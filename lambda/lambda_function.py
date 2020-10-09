# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

#######################################################
from ask_sdk_core.utils import get_supported_interfaces
#######################################################
import sys
import random


from ask_sdk_model import Response
#########################################################
import json

def _load_apl_document(file_path):
    # type: (str) -> Dict[str, Any]
    """Load the apl json document at the path into a dict object."""
    with open(file_path) as f:
        return json.load(f)

from ask_sdk_model.interfaces.alexa.presentation.apl import (
	    RenderDocumentDirective, ExecuteCommandsDirective, SpeakItemCommand,
	    AutoPageCommand, HighlightMode)
##########################################################


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

arregloPalabras = ["verde","rojo","azul"]
accessArray = (random.choice(arregloPalabras))



class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        #speak_output = accessArray
        """
        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )"""
        speak_output = "Intenta leer la palabra"
        

        if accessArray == "azul" and get_supported_interfaces(handler_input).alexa_presentation_apl is not None: 
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask("A reprompt to keep the session open")
                    .add_directive(
                        RenderDocumentDirective(
                            token="pagerToken",
                            document=_load_apl_document("azul.json"),
                            datasources={}
                        )
                    )
                    .response
                )
        elif accessArray == "rojo" and get_supported_interfaces(handler_input).alexa_presentation_apl is not None: 
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask("A reprompt to keep the session open")
                    .add_directive(
                        RenderDocumentDirective(
                            token="pagerToken",
                            document=_load_apl_document("rojo.json"),
                            datasources={}
                        )
                    )
                    .response
                )
        
        elif accessArray == "verde" and get_supported_interfaces(handler_input).alexa_presentation_apl is not None: 
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask("A reprompt to keep the session open")
                    .add_directive(
                        RenderDocumentDirective(
                            token="pagerToken",
                            document=_load_apl_document("verde.json"),
                            datasources={}
                        )
                    )
                    .response
                )
        
        
        else:
            speak_output = "You don't have a screen"
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask("Please buy an Alexa device with a screen")
                    .response
            )
        

class CapturaPalabraIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CapturaPalabraIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        varPalabra = slots["palabra"].value
        
        
        if varPalabra == accessArray:
            speak_output = "Bien hecho!"

        else:
            speak_output = "Intenta de nuevo"
        
        return (
            
            handler_input.response_builder
                .speak(speak_output)
                #.ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "¡Hasta luego!"

        return (
            
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.
        logger.info("In SessionEndedRequestHandler")
        #session("sb") = ""
        apeak_output = "Terminar Sesion"
        

        return handler_input.response_builder.respose  


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Lo siento, tengo problemas para realizar lo que me pides. Intenta de nuevo"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CapturaPalabraIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()