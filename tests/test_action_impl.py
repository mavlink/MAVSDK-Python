# -*- coding: utf-8 -*-
import unittest
from dronecore import Action
from dronecore.generated import action_pb2


class TestActionPlugin(unittest.TestCase):

    # ActionResults when the command succeeds
    SUCCESS_RESULTS = [
            action_pb2.ActionResult.SUCCESS
    ]

    # ActionResults with a detected failure
    ERROR_RESULTS = [
            action_pb2.ActionResult.BUSY,
            action_pb2.ActionResult.COMMAND_DENIED,
            action_pb2.ActionResult.COMMAND_DENIED_NOT_LANDED,
            action_pb2.ActionResult.COMMAND_DENIED_LANDED_STATE_UNKNOWN,
            action_pb2.ActionResult.CONNECTION_ERROR,
            action_pb2.ActionResult.NO_SYSTEM,
            action_pb2.ActionResult.NO_VTOL_TRANSITION_SUPPORT,
            action_pb2.ActionResult.TIMEOUT,
            action_pb2.ActionResult.UNKNOWN,
            action_pb2.ActionResult.VTOL_TRANSITION_SUPPORT_UNKNOWN,
    ]

    def fake_response(self, response, result):
        """
        Sets the result of a response
        """
        response.action_result.result = result
        return response

    def fake_arm_response(self, result):
        """
        Generates a fake arm response
        """
        return self.fake_response(action_pb2.ArmResponse(),
                                  result)

    def fake_disarm_response(self, result):
        """
        Generates a fake disarm response
        """
        return self.fake_response(action_pb2.DisarmResponse(),
                                  result)

    def fake_takeoff_response(self, result):
        """
        Generates a fake takeoff response
        """
        return self.fake_response(action_pb2.TakeoffResponse(),
                                  result)

#   @TODO does not seem to have a action_result
#   def fake_set_takeoff_altitude_response(self, result):
#       """
#       Generates a fake set takeoff altitude response
#       """
#       return self.fake_response(action_pb2.SetTakeoffAltitudeResponse(),
#                                 result)
#
#   def fake_get_takeoff_altitude_response(self, result):
#       """
#       Generates a fake set takeoff altitude response
#       """
#       return self.fake_response(action_pb2.GetTakeoffAltitudeResponse(),
#                                 result)

    def fake_land_response(self, result):
        """
        Generates a fake land response
        """
        return self.fake_response(action_pb2.LandResponse(),
                                  result)

    def test_plugin_name(self):
        """
        Tests if the plugin name is correct
        """
        self.assertTrue(Action().name == "Action")

    def test_arm_success(self):
        """
        Tests if a successfull arm is detected
        """
        for result in self.SUCCESS_RESULTS:
            self.assertTrue(Action()._response_success(
                self.fake_arm_response(result)
            ))

    def test_arm_failed(self):
        """
        Tests if an error during arming is detected
        """
        for result in self.ERROR_RESULTS:
            self.assertFalse(Action()._response_success(
                self.fake_arm_response(result)
            ))

    def test_disarm_success(self):
        """
        Tests if a successfull disarm is detected
        """
        for result in self.SUCCESS_RESULTS:
            self.assertTrue(Action()._response_success(
                self.fake_disarm_response(result)
            ))

    def test_disarm_failed(self):
        """
        Tests if an error during disarming is detected
        """
        for result in self.ERROR_RESULTS:
            self.assertFalse(Action()._response_success(
                self.fake_disarm_response(result)
            ))

    def test_takeoff_success(self):
        """
        Tests if a successfull takeoff is detected
        """
        for result in self.SUCCESS_RESULTS:
            self.assertTrue(Action()._response_success(
                self.fake_takeoff_response(result)
            ))

    def test_takeoff_failed(self):
        """
        Tests if a successfull takeoff is detected
        """
        for result in self.ERROR_RESULTS:
            self.assertFalse(Action()._response_success(
                self.fake_takeoff_response(result)
            ))

#   @TODO seems to not be working, check with actual response
#   def test_set_takeoff_altitude_success(self):
#       """
#       Tests if setting the takeoff altitude was successfull
#       """
#       for result in self.SUCCESS_RESULTS:
#           self.assertTrue(Action()._response_success(
#               self.fake_set_takeoff_altitude_response(result)
#           ))
#
#
#   def test_set_takeoff_altitude_failed(self):
#       """
#       Tests if setting the takeoff altitudefailed
#       """
#       for result in self.ERROR_RESULTS:
#           self.assertFailed(Action()._response_success(
#               self.fake_set_takeoff_altitude_response(result)
#           ))
#
#   def test_get_takeoff_altitude_success(self):
#       """
#       Tests if getting the takeoff altitude was successfull
#       """
#       for result in self.SUCCESS_RESULTS:
#           self.assertTrue(Action()._response_success(
#               self.fake_get_takeoff_altitude_response(result)
#           ))
#
#   def test_get_takeoff_altitude_failed(self):
#       """
#       Tests if getting the takeoff altitudefailed
#       """
#       for result in self.ERROR_RESULTS:
#           self.assertFailed(Action()._response_success(
#               self.fake_get_takeoff_altitude_response(result)
#           ))

    def test_land_success(self):
        """
        Tests if a successfull land is detected
        """
        for result in self.SUCCESS_RESULTS:
            self.assertTrue(Action()._response_success(
                self.fake_land_response(result)
            ))

    def test_land_failed(self):
        """
        Tests if an error during landing is detected
        """
        for result in self.ERROR_RESULTS:
            self.assertFalse(Action()._response_success(
                self.fake_land_response(result)
            ))
