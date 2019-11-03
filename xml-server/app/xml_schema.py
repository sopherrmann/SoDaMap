# ./xml_schema.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2019-10-17 11:39:10.404036 by PyXB version 1.2.6 using Python 3.6.4.final.0
# Namespace AbsentNamespace0

# from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f8b49b50-f0c1-11e9-9324-303a6417ae62')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])


def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type suggestions with content type ELEMENT_ONLY
class suggestions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type suggestions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'suggestions')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 6, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element suggestion uses Python identifier suggestion
    __suggestion = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'suggestion'), 'suggestion', '__AbsentNamespace0_suggestions_suggestion', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 8, 6), )


    suggestion = property(__suggestion.value, __suggestion.set, None, None)

    _ElementMap.update({
        __suggestion.name() : __suggestion
    })
    _AttributeMap.update({

    })
_module_typeBindings.suggestions = suggestions
Namespace.addCategoryObject('typeBinding', 'suggestions', suggestions)


# Complex type geocoordinateWithTimeStamp with content type ELEMENT_ONLY
class geocoordinateWithTimeStamp (pyxb.binding.basis.complexTypeDefinition):
    """Complex type geocoordinateWithTimeStamp with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'geocoordinateWithTimeStamp')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 15, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element latitude uses Python identifier latitude
    __latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'latitude'), 'latitude', '__AbsentNamespace0_geocoordinateWithTimeStamp_latitude', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 17, 6), )


    latitude = property(__latitude.value, __latitude.set, None, None)


    # Element longitude uses Python identifier longitude
    __longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'longitude'), 'longitude', '__AbsentNamespace0_geocoordinateWithTimeStamp_longitude', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 18, 6), )


    longitude = property(__longitude.value, __longitude.set, None, None)


    # Element timeStamp uses Python identifier timeStamp
    __timeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'timeStamp'), 'timeStamp', '__AbsentNamespace0_geocoordinateWithTimeStamp_timeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 19, 6), )


    timeStamp = property(__timeStamp.value, __timeStamp.set, None, None)

    _ElementMap.update({
        __latitude.name() : __latitude,
        __longitude.name() : __longitude,
        __timeStamp.name() : __timeStamp
    })
    _AttributeMap.update({

    })
_module_typeBindings.geocoordinateWithTimeStamp = geocoordinateWithTimeStamp
Namespace.addCategoryObject('typeBinding', 'geocoordinateWithTimeStamp', geocoordinateWithTimeStamp)


# Complex type bbox with content type ELEMENT_ONLY
class bbox (pyxb.binding.basis.complexTypeDefinition):
    """Complex type bbox with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bbox')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 26, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element upperLeftCorner uses Python identifier upperLeftCorner
    __upperLeftCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'upperLeftCorner'), 'upperLeftCorner', '__AbsentNamespace0_bbox_upperLeftCorner', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 28, 6), )


    upperLeftCorner = property(__upperLeftCorner.value, __upperLeftCorner.set, None, None)


    # Element lowerRightCorner uses Python identifier lowerRightCorner
    __lowerRightCorner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lowerRightCorner'), 'lowerRightCorner', '__AbsentNamespace0_bbox_lowerRightCorner', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 29, 6), )


    lowerRightCorner = property(__lowerRightCorner.value, __lowerRightCorner.set, None, None)

    _ElementMap.update({
        __upperLeftCorner.name() : __upperLeftCorner,
        __lowerRightCorner.name() : __lowerRightCorner
    })
    _AttributeMap.update({

    })
_module_typeBindings.bbox = bbox
Namespace.addCategoryObject('typeBinding', 'bbox', bbox)


# Complex type questionStruct with content type ELEMENT_ONLY
class questionStruct (pyxb.binding.basis.complexTypeDefinition):
    """Complex type questionStruct with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'questionStruct')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 35, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element question uses Python identifier question
    __question = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'question'), 'question', '__AbsentNamespace0_questionStruct_question', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 37, 6), )


    question = property(__question.value, __question.set, None, None)


    # Element answer uses Python identifier answer
    __answer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'answer'), 'answer', '__AbsentNamespace0_questionStruct_answer', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 38, 6), )


    answer = property(__answer.value, __answer.set, None, None)

    _ElementMap.update({
        __question.name() : __question,
        __answer.name() : __answer
    })
    _AttributeMap.update({

    })
_module_typeBindings.questionStruct = questionStruct
Namespace.addCategoryObject('typeBinding', 'questionStruct', questionStruct)


# Complex type questions with content type ELEMENT_ONLY
class questions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type questions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'questions')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 45, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element question uses Python identifier question
    __question = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'question'), 'question', '__AbsentNamespace0_questions_question', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 47, 6), )


    question = property(__question.value, __question.set, None, None)

    _ElementMap.update({
        __question.name() : __question
    })
    _AttributeMap.update({

    })
_module_typeBindings.questions = questions
Namespace.addCategoryObject('typeBinding', 'questions', questions)


# Complex type textWithSuggestions with content type ELEMENT_ONLY
class textWithSuggestions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type textWithSuggestions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'textWithSuggestions')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element textTyped uses Python identifier textTyped
    __textTyped = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'textTyped'), 'textTyped', '__AbsentNamespace0_textWithSuggestions_textTyped', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 56, 6), )


    textTyped = property(__textTyped.value, __textTyped.set, None, None)


    # Element suggestions uses Python identifier suggestions
    __suggestions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'suggestions'), 'suggestions', '__AbsentNamespace0_textWithSuggestions_suggestions', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 57, 5), )


    suggestions = property(__suggestions.value, __suggestions.set, None, None)


    # Element suggestionChosen uses Python identifier suggestionChosen
    __suggestionChosen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'suggestionChosen'), 'suggestionChosen', '__AbsentNamespace0_textWithSuggestions_suggestionChosen', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 58, 5), )


    suggestionChosen = property(__suggestionChosen.value, __suggestionChosen.set, None, None)

    _ElementMap.update({
        __textTyped.name() : __textTyped,
        __suggestions.name() : __suggestions,
        __suggestionChosen.name() : __suggestionChosen
    })
    _AttributeMap.update({

    })
_module_typeBindings.textWithSuggestions = textWithSuggestions
Namespace.addCategoryObject('typeBinding', 'textWithSuggestions', textWithSuggestions)


# Complex type zoomInOut with content type ELEMENT_ONLY
class zoomInOut (pyxb.binding.basis.complexTypeDefinition):
    """Complex type zoomInOut with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'zoomInOut')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element oldZoomLevel uses Python identifier oldZoomLevel
    __oldZoomLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'oldZoomLevel'), 'oldZoomLevel', '__AbsentNamespace0_zoomInOut_oldZoomLevel', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 67, 6), )


    oldZoomLevel = property(__oldZoomLevel.value, __oldZoomLevel.set, None, None)


    # Element newZoomLevel uses Python identifier newZoomLevel
    __newZoomLevel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'newZoomLevel'), 'newZoomLevel', '__AbsentNamespace0_zoomInOut_newZoomLevel', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 68, 6), )


    newZoomLevel = property(__newZoomLevel.value, __newZoomLevel.set, None, None)


    # Element oldBBox uses Python identifier oldBBox
    __oldBBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'oldBBox'), 'oldBBox', '__AbsentNamespace0_zoomInOut_oldBBox', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 69, 6), )


    oldBBox = property(__oldBBox.value, __oldBBox.set, None, None)


    # Element newBBox uses Python identifier newBBox
    __newBBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'newBBox'), 'newBBox', '__AbsentNamespace0_zoomInOut_newBBox', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 70, 6), )


    newBBox = property(__newBBox.value, __newBBox.set, None, None)

    _ElementMap.update({
        __oldZoomLevel.name() : __oldZoomLevel,
        __newZoomLevel.name() : __newZoomLevel,
        __oldBBox.name() : __oldBBox,
        __newBBox.name() : __newBBox
    })
    _AttributeMap.update({

    })
_module_typeBindings.zoomInOut = zoomInOut
Namespace.addCategoryObject('typeBinding', 'zoomInOut', zoomInOut)


# Complex type click with content type ELEMENT_ONLY
class click (pyxb.binding.basis.complexTypeDefinition):
    """Complex type click with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'click')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 76, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element whereClicked uses Python identifier whereClicked
    __whereClicked = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'whereClicked'), 'whereClicked', '__AbsentNamespace0_click_whereClicked', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 78, 6), )


    whereClicked = property(__whereClicked.value, __whereClicked.set, None, None)


    # Element BBox uses Python identifier BBox
    __BBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BBox'), 'BBox', '__AbsentNamespace0_click_BBox', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 79, 6), )


    BBox = property(__BBox.value, __BBox.set, None, None)

    _ElementMap.update({
        __whereClicked.name() : __whereClicked,
        __BBox.name() : __BBox
    })
    _AttributeMap.update({

    })
_module_typeBindings.click = click
Namespace.addCategoryObject('typeBinding', 'click', click)


# Complex type pan with content type ELEMENT_ONLY
class pan (pyxb.binding.basis.complexTypeDefinition):
    """Complex type pan with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'pan')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 86, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element oldBBox uses Python identifier oldBBox
    __oldBBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'oldBBox'), 'oldBBox', '__AbsentNamespace0_pan_oldBBox', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 88, 6), )


    oldBBox = property(__oldBBox.value, __oldBBox.set, None, None)


    # Element newBBox uses Python identifier newBBox
    __newBBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'newBBox'), 'newBBox', '__AbsentNamespace0_pan_newBBox', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 89, 6), )


    newBBox = property(__newBBox.value, __newBBox.set, None, None)

    _ElementMap.update({
        __oldBBox.name() : __oldBBox,
        __newBBox.name() : __newBBox
    })
    _AttributeMap.update({

    })
_module_typeBindings.pan = pan
Namespace.addCategoryObject('typeBinding', 'pan', pan)


# Complex type mapInteractionType with content type ELEMENT_ONLY
class mapInteractionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type mapInteractionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mapInteractionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 95, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element zoomInInteraction uses Python identifier zoomInInteraction
    __zoomInInteraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'zoomInInteraction'), 'zoomInInteraction', '__AbsentNamespace0_mapInteractionType_zoomInInteraction', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 97, 6), )


    zoomInInteraction = property(__zoomInInteraction.value, __zoomInInteraction.set, None, None)


    # Element zoomOutInteraction uses Python identifier zoomOutInteraction
    __zoomOutInteraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'zoomOutInteraction'), 'zoomOutInteraction', '__AbsentNamespace0_mapInteractionType_zoomOutInteraction', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 98, 6), )


    zoomOutInteraction = property(__zoomOutInteraction.value, __zoomOutInteraction.set, None, None)


    # Element clickInteraction uses Python identifier clickInteraction
    __clickInteraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'clickInteraction'), 'clickInteraction', '__AbsentNamespace0_mapInteractionType_clickInteraction', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 99, 6), )


    clickInteraction = property(__clickInteraction.value, __clickInteraction.set, None, None)


    # Element panInteraction uses Python identifier panInteraction
    __panInteraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'panInteraction'), 'panInteraction', '__AbsentNamespace0_mapInteractionType_panInteraction', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 100, 6), )


    panInteraction = property(__panInteraction.value, __panInteraction.set, None, None)

    _ElementMap.update({
        __zoomInInteraction.name() : __zoomInInteraction,
        __zoomOutInteraction.name() : __zoomOutInteraction,
        __clickInteraction.name() : __clickInteraction,
        __panInteraction.name() : __panInteraction
    })
    _AttributeMap.update({

    })
_module_typeBindings.mapInteractionType = mapInteractionType
Namespace.addCategoryObject('typeBinding', 'mapInteractionType', mapInteractionType)


# Complex type userPositions with content type ELEMENT_ONLY
class userPositions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type userPositions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'userPositions')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 108, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element userPosition uses Python identifier userPosition
    __userPosition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'userPosition'), 'userPosition', '__AbsentNamespace0_userPositions_userPosition', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 110, 6), )


    userPosition = property(__userPosition.value, __userPosition.set, None, None)

    _ElementMap.update({
        __userPosition.name() : __userPosition
    })
    _AttributeMap.update({

    })
_module_typeBindings.userPositions = userPositions
Namespace.addCategoryObject('typeBinding', 'userPositions', userPositions)


# Complex type mapInteraction with content type ELEMENT_ONLY
class mapInteraction (pyxb.binding.basis.complexTypeDefinition):
    """Complex type mapInteraction with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mapInteraction')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 118, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element userPositionWithTimeStamp uses Python identifier userPositionWithTimeStamp
    __userPositionWithTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'userPositionWithTimeStamp'), 'userPositionWithTimeStamp', '__AbsentNamespace0_mapInteraction_userPositionWithTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 120, 6), )


    userPositionWithTimeStamp = property(__userPositionWithTimeStamp.value, __userPositionWithTimeStamp.set, None, None)


    # Element mapInteractionTypeName uses Python identifier mapInteractionTypeName
    __mapInteractionTypeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mapInteractionTypeName'), 'mapInteractionTypeName', '__AbsentNamespace0_mapInteraction_mapInteractionTypeName', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 121, 6), )


    mapInteractionTypeName = property(__mapInteractionTypeName.value, __mapInteractionTypeName.set, None, None)

    _ElementMap.update({
        __userPositionWithTimeStamp.name() : __userPositionWithTimeStamp,
        __mapInteractionTypeName.name() : __mapInteractionTypeName
    })
    _AttributeMap.update({

    })
_module_typeBindings.mapInteraction = mapInteraction
Namespace.addCategoryObject('typeBinding', 'mapInteraction', mapInteraction)


# Complex type mapInteractions with content type ELEMENT_ONLY
class mapInteractions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type mapInteractions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mapInteractions')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 127, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element singleMapInteraction uses Python identifier singleMapInteraction
    __singleMapInteraction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'singleMapInteraction'), 'singleMapInteraction', '__AbsentNamespace0_mapInteractions_singleMapInteraction', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 129, 6), )


    singleMapInteraction = property(__singleMapInteraction.value, __singleMapInteraction.set, None, None)

    _ElementMap.update({
        __singleMapInteraction.name() : __singleMapInteraction
    })
    _AttributeMap.update({

    })
_module_typeBindings.mapInteractions = mapInteractions
Namespace.addCategoryObject('typeBinding', 'mapInteractions', mapInteractions)


# Complex type mapSearch with content type ELEMENT_ONLY
class mapSearch (pyxb.binding.basis.complexTypeDefinition):
    """Complex type mapSearch with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mapSearch')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 136, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element StarttimeStamp uses Python identifier StarttimeStamp
    __StarttimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'StarttimeStamp'), 'StarttimeStamp', '__AbsentNamespace0_mapSearch_StarttimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 138, 6), )


    StarttimeStamp = property(__StarttimeStamp.value, __StarttimeStamp.set, None, None)


    # Element EndtimeStamp uses Python identifier EndtimeStamp
    __EndtimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'EndtimeStamp'), 'EndtimeStamp', '__AbsentNamespace0_mapSearch_EndtimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 139, 6), )


    EndtimeStamp = property(__EndtimeStamp.value, __EndtimeStamp.set, None, None)


    # Element BBox uses Python identifier BBox
    __BBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'BBox'), 'BBox', '__AbsentNamespace0_mapSearch_BBox', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 140, 6), )


    BBox = property(__BBox.value, __BBox.set, None, None)


    # Element textWithSuggestions uses Python identifier textWithSuggestions
    __textWithSuggestions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'textWithSuggestions'), 'textWithSuggestions', '__AbsentNamespace0_mapSearch_textWithSuggestions', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 141, 6), )


    textWithSuggestions = property(__textWithSuggestions.value, __textWithSuggestions.set, None, None)

    _ElementMap.update({
        __StarttimeStamp.name() : __StarttimeStamp,
        __EndtimeStamp.name() : __EndtimeStamp,
        __BBox.name() : __BBox,
        __textWithSuggestions.name() : __textWithSuggestions
    })
    _AttributeMap.update({

    })
_module_typeBindings.mapSearch = mapSearch
Namespace.addCategoryObject('typeBinding', 'mapSearch', mapSearch)


# Complex type mapSearchs with content type ELEMENT_ONLY
class mapSearchs (pyxb.binding.basis.complexTypeDefinition):
    """Complex type mapSearchs with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mapSearchs')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 148, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element mapSearchElement uses Python identifier mapSearchElement
    __mapSearchElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mapSearchElement'), 'mapSearchElement', '__AbsentNamespace0_mapSearchs_mapSearchElement', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 150, 6), )


    mapSearchElement = property(__mapSearchElement.value, __mapSearchElement.set, None, None)

    _ElementMap.update({
        __mapSearchElement.name() : __mapSearchElement
    })
    _AttributeMap.update({

    })
_module_typeBindings.mapSearchs = mapSearchs
Namespace.addCategoryObject('typeBinding', 'mapSearchs', mapSearchs)


# Complex type routing with content type ELEMENT_ONLY
class routing (pyxb.binding.basis.complexTypeDefinition):
    """Complex type routing with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routing')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 157, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element startRoutingInterfaceTimeStamp uses Python identifier startRoutingInterfaceTimeStamp
    __startRoutingInterfaceTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'startRoutingInterfaceTimeStamp'), 'startRoutingInterfaceTimeStamp', '__AbsentNamespace0_routing_startRoutingInterfaceTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 159, 5), )


    startRoutingInterfaceTimeStamp = property(__startRoutingInterfaceTimeStamp.value, __startRoutingInterfaceTimeStamp.set, None, None)


    # Element endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp uses Python identifier endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp
    __endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp'), 'endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp', '__AbsentNamespace0_routing_endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 160, 5), )


    endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp = property(__endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp.value, __endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp.set, None, None)


    # Element startRoutingTimeStamp uses Python identifier startRoutingTimeStamp
    __startRoutingTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'startRoutingTimeStamp'), 'startRoutingTimeStamp', '__AbsentNamespace0_routing_startRoutingTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 161, 5), )


    startRoutingTimeStamp = property(__startRoutingTimeStamp.value, __startRoutingTimeStamp.set, None, None)


    # Element endRoutingTimeStamp uses Python identifier endRoutingTimeStamp
    __endRoutingTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'endRoutingTimeStamp'), 'endRoutingTimeStamp', '__AbsentNamespace0_routing_endRoutingTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 162, 5), )


    endRoutingTimeStamp = property(__endRoutingTimeStamp.value, __endRoutingTimeStamp.set, None, None)


    # Element OriginTextBoxHistory uses Python identifier OriginTextBoxHistory
    __OriginTextBoxHistory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OriginTextBoxHistory'), 'OriginTextBoxHistory', '__AbsentNamespace0_routing_OriginTextBoxHistory', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 163, 5), )


    OriginTextBoxHistory = property(__OriginTextBoxHistory.value, __OriginTextBoxHistory.set, None, None)


    # Element DestiantionTextBoxHistory uses Python identifier DestiantionTextBoxHistory
    __DestiantionTextBoxHistory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'DestiantionTextBoxHistory'), 'DestiantionTextBoxHistory', '__AbsentNamespace0_routing_DestiantionTextBoxHistory', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 164, 5), )


    DestiantionTextBoxHistory = property(__DestiantionTextBoxHistory.value, __DestiantionTextBoxHistory.set, None, None)

    _ElementMap.update({
        __startRoutingInterfaceTimeStamp.name() : __startRoutingInterfaceTimeStamp,
        __endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp.name() : __endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp,
        __startRoutingTimeStamp.name() : __startRoutingTimeStamp,
        __endRoutingTimeStamp.name() : __endRoutingTimeStamp,
        __OriginTextBoxHistory.name() : __OriginTextBoxHistory,
        __DestiantionTextBoxHistory.name() : __DestiantionTextBoxHistory
    })
    _AttributeMap.update({

    })
_module_typeBindings.routing = routing
Namespace.addCategoryObject('typeBinding', 'routing', routing)


# Complex type routings with content type ELEMENT_ONLY
class routings (pyxb.binding.basis.complexTypeDefinition):
    """Complex type routings with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routings')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 171, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element routingElement uses Python identifier routingElement
    __routingElement = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routingElement'), 'routingElement', '__AbsentNamespace0_routings_routingElement', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 173, 5), )


    routingElement = property(__routingElement.value, __routingElement.set, None, None)

    _ElementMap.update({
        __routingElement.name() : __routingElement
    })
    _AttributeMap.update({

    })
_module_typeBindings.routings = routings
Namespace.addCategoryObject('typeBinding', 'routings', routings)


# Complex type spatialBookmark with content type ELEMENT_ONLY
class spatialBookmark (pyxb.binding.basis.complexTypeDefinition):
    """Complex type spatialBookmark with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spatialBookmark')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 180, 0)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element userPositionWithTimeStamp uses Python identifier userPositionWithTimeStamp
    __userPositionWithTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'userPositionWithTimeStamp'), 'userPositionWithTimeStamp', '__AbsentNamespace0_spatialBookmark_userPositionWithTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 182, 6), )


    userPositionWithTimeStamp = property(__userPositionWithTimeStamp.value, __userPositionWithTimeStamp.set, None, None)


    # Element notes uses Python identifier notes
    __notes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'notes'), 'notes', '__AbsentNamespace0_spatialBookmark_notes', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 183, 6), )


    notes = property(__notes.value, __notes.set, None, None)

    _ElementMap.update({
        __userPositionWithTimeStamp.name() : __userPositionWithTimeStamp,
        __notes.name() : __notes
    })
    _AttributeMap.update({

    })
_module_typeBindings.spatialBookmark = spatialBookmark
Namespace.addCategoryObject('typeBinding', 'spatialBookmark', spatialBookmark)


# Complex type spatialBookmarks with content type ELEMENT_ONLY
class spatialBookmarks (pyxb.binding.basis.complexTypeDefinition):
    """Complex type spatialBookmarks with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'spatialBookmarks')
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 191, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element spatialBookmark uses Python identifier spatialBookmark
    __spatialBookmark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'spatialBookmark'), 'spatialBookmark', '__AbsentNamespace0_spatialBookmarks_spatialBookmark', True, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 193, 6), )


    spatialBookmark = property(__spatialBookmark.value, __spatialBookmark.set, None, None)

    _ElementMap.update({
        __spatialBookmark.name() : __spatialBookmark
    })
    _AttributeMap.update({

    })
_module_typeBindings.spatialBookmarks = spatialBookmarks
Namespace.addCategoryObject('typeBinding', 'spatialBookmarks', spatialBookmarks)


# Complex type [anonymous] with content type ELEMENT_ONLY
class MappedSession (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 201, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element startApplicationTimeStamp uses Python identifier startApplicationTimeStamp
    __startApplicationTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'startApplicationTimeStamp'), 'startApplicationTimeStamp', '__AbsentNamespace0_CTD_ANON_startApplicationTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 203, 6), )


    startApplicationTimeStamp = property(__startApplicationTimeStamp.value, __startApplicationTimeStamp.set, None, None)


    # Element endApplicationTimeStamp uses Python identifier endApplicationTimeStamp
    __endApplicationTimeStamp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'endApplicationTimeStamp'), 'endApplicationTimeStamp', '__AbsentNamespace0_CTD_ANON_endApplicationTimeStamp', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 204, 6), )


    endApplicationTimeStamp = property(__endApplicationTimeStamp.value, __endApplicationTimeStamp.set, None, None)


    # Element userPositionElements uses Python identifier userPositionElements
    __userPositionElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'userPositionElements'), 'userPositionElements', '__AbsentNamespace0_CTD_ANON_userPositionElements', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 205, 6), )


    userPositionElements = property(__userPositionElements.value, __userPositionElements.set, None, None)


    # Element mapInteractionsElements uses Python identifier mapInteractionsElements
    __mapInteractionsElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mapInteractionsElements'), 'mapInteractionsElements', '__AbsentNamespace0_CTD_ANON_mapInteractionsElements', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 206, 6), )


    mapInteractionsElements = property(__mapInteractionsElements.value, __mapInteractionsElements.set, None, None)


    # Element mapSearchsElements uses Python identifier mapSearchsElements
    __mapSearchsElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mapSearchsElements'), 'mapSearchsElements', '__AbsentNamespace0_CTD_ANON_mapSearchsElements', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 207, 6), )


    mapSearchsElements = property(__mapSearchsElements.value, __mapSearchsElements.set, None, None)


    # Element routingsElements uses Python identifier routingsElements
    __routingsElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routingsElements'), 'routingsElements', '__AbsentNamespace0_CTD_ANON_routingsElements', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 208, 6), )


    routingsElements = property(__routingsElements.value, __routingsElements.set, None, None)


    # Element questionsElements uses Python identifier questionsElements
    __questionsElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'questionsElements'), 'questionsElements', '__AbsentNamespace0_CTD_ANON_questionsElements', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 209, 6), )


    questionsElements = property(__questionsElements.value, __questionsElements.set, None, None)


    # Element spatialBookmarksElements uses Python identifier spatialBookmarksElements
    __spatialBookmarksElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'spatialBookmarksElements'), 'spatialBookmarksElements', '__AbsentNamespace0_CTD_ANON_spatialBookmarksElements', False, pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 210, 6), )


    spatialBookmarksElements = property(__spatialBookmarksElements.value, __spatialBookmarksElements.set, None, None)

    _ElementMap.update({
        __startApplicationTimeStamp.name() : __startApplicationTimeStamp,
        __endApplicationTimeStamp.name() : __endApplicationTimeStamp,
        __userPositionElements.name() : __userPositionElements,
        __mapInteractionsElements.name() : __mapInteractionsElements,
        __mapSearchsElements.name() : __mapSearchsElements,
        __routingsElements.name() : __routingsElements,
        __questionsElements.name() : __questionsElements,
        __spatialBookmarksElements.name() : __spatialBookmarksElements
    })
    _AttributeMap.update({

    })
_module_typeBindings.CTD_ANON = MappedSession


outputFile = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outputFile'), MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 200, 0))
Namespace.addCategoryObject('elementBinding', outputFile.name().localName(), outputFile)



suggestions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'suggestion'), pyxb.binding.datatypes.string, scope=suggestions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 8, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 8, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(suggestions._UseForTag(pyxb.namespace.ExpandedName(None, 'suggestion')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
suggestions._Automaton = _BuildAutomaton()




geocoordinateWithTimeStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'latitude'), pyxb.binding.datatypes.decimal, scope=geocoordinateWithTimeStamp, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 17, 6)))

geocoordinateWithTimeStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'longitude'), pyxb.binding.datatypes.decimal, scope=geocoordinateWithTimeStamp, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 18, 6)))

geocoordinateWithTimeStamp._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'timeStamp'), pyxb.binding.datatypes.dateTime, scope=geocoordinateWithTimeStamp, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 19, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geocoordinateWithTimeStamp._UseForTag(pyxb.namespace.ExpandedName(None, 'latitude')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 17, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(geocoordinateWithTimeStamp._UseForTag(pyxb.namespace.ExpandedName(None, 'longitude')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 18, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(geocoordinateWithTimeStamp._UseForTag(pyxb.namespace.ExpandedName(None, 'timeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 19, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
geocoordinateWithTimeStamp._Automaton = _BuildAutomaton_()




bbox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'upperLeftCorner'), geocoordinateWithTimeStamp, scope=bbox, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 28, 6)))

bbox._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lowerRightCorner'), geocoordinateWithTimeStamp, scope=bbox, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 29, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(bbox._UseForTag(pyxb.namespace.ExpandedName(None, 'upperLeftCorner')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 28, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(bbox._UseForTag(pyxb.namespace.ExpandedName(None, 'lowerRightCorner')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 29, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
bbox._Automaton = _BuildAutomaton_2()




questionStruct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'question'), pyxb.binding.datatypes.string, scope=questionStruct, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 37, 6)))

questionStruct._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'answer'), pyxb.binding.datatypes.string, scope=questionStruct, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 38, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(questionStruct._UseForTag(pyxb.namespace.ExpandedName(None, 'question')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 37, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(questionStruct._UseForTag(pyxb.namespace.ExpandedName(None, 'answer')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 38, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
questionStruct._Automaton = _BuildAutomaton_3()




questions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'question'), questionStruct, scope=questions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 47, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(questions._UseForTag(pyxb.namespace.ExpandedName(None, 'question')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 47, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
    ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
questions._Automaton = _BuildAutomaton_4()




textWithSuggestions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'textTyped'), pyxb.binding.datatypes.string, scope=textWithSuggestions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 56, 6)))

textWithSuggestions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'suggestions'), suggestions, scope=textWithSuggestions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 57, 5)))

textWithSuggestions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'suggestionChosen'), pyxb.binding.datatypes.string, scope=textWithSuggestions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 58, 5)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 57, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 58, 5))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(textWithSuggestions._UseForTag(pyxb.namespace.ExpandedName(None, 'textTyped')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(textWithSuggestions._UseForTag(pyxb.namespace.ExpandedName(None, 'suggestions')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 57, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(textWithSuggestions._UseForTag(pyxb.namespace.ExpandedName(None, 'suggestionChosen')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 58, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
textWithSuggestions._Automaton = _BuildAutomaton_5()




zoomInOut._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'oldZoomLevel'), pyxb.binding.datatypes.integer, scope=zoomInOut, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 67, 6)))

zoomInOut._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'newZoomLevel'), pyxb.binding.datatypes.integer, scope=zoomInOut, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 68, 6)))

zoomInOut._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'oldBBox'), bbox, scope=zoomInOut, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 69, 6)))

zoomInOut._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'newBBox'), bbox, scope=zoomInOut, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 70, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(zoomInOut._UseForTag(pyxb.namespace.ExpandedName(None, 'oldZoomLevel')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 67, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(zoomInOut._UseForTag(pyxb.namespace.ExpandedName(None, 'newZoomLevel')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 68, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(zoomInOut._UseForTag(pyxb.namespace.ExpandedName(None, 'oldBBox')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 69, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(zoomInOut._UseForTag(pyxb.namespace.ExpandedName(None, 'newBBox')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 70, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
zoomInOut._Automaton = _BuildAutomaton_6()




click._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'whereClicked'), geocoordinateWithTimeStamp, scope=click, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 78, 6)))

click._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BBox'), bbox, scope=click, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 79, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(click._UseForTag(pyxb.namespace.ExpandedName(None, 'whereClicked')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 78, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(click._UseForTag(pyxb.namespace.ExpandedName(None, 'BBox')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 79, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
click._Automaton = _BuildAutomaton_7()




pan._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'oldBBox'), bbox, scope=pan, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 88, 6)))

pan._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'newBBox'), bbox, scope=pan, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 89, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(pan._UseForTag(pyxb.namespace.ExpandedName(None, 'oldBBox')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 88, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(pan._UseForTag(pyxb.namespace.ExpandedName(None, 'newBBox')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 89, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
pan._Automaton = _BuildAutomaton_8()




mapInteractionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'zoomInInteraction'), zoomInOut, scope=mapInteractionType, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 97, 6)))

mapInteractionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'zoomOutInteraction'), zoomInOut, scope=mapInteractionType, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 98, 6)))

mapInteractionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'clickInteraction'), click, scope=mapInteractionType, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 99, 6)))

mapInteractionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'panInteraction'), pan, scope=mapInteractionType, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 100, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mapInteractionType._UseForTag(pyxb.namespace.ExpandedName(None, 'zoomInInteraction')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 97, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mapInteractionType._UseForTag(pyxb.namespace.ExpandedName(None, 'zoomOutInteraction')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 98, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mapInteractionType._UseForTag(pyxb.namespace.ExpandedName(None, 'clickInteraction')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 99, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mapInteractionType._UseForTag(pyxb.namespace.ExpandedName(None, 'panInteraction')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 100, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mapInteractionType._Automaton = _BuildAutomaton_9()




userPositions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'userPosition'), geocoordinateWithTimeStamp, scope=userPositions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 110, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(userPositions._UseForTag(pyxb.namespace.ExpandedName(None, 'userPosition')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 110, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
    ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
userPositions._Automaton = _BuildAutomaton_10()




mapInteraction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'userPositionWithTimeStamp'), geocoordinateWithTimeStamp, scope=mapInteraction, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 120, 6)))

mapInteraction._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mapInteractionTypeName'), mapInteractionType, scope=mapInteraction, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 121, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mapInteraction._UseForTag(pyxb.namespace.ExpandedName(None, 'userPositionWithTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 120, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mapInteraction._UseForTag(pyxb.namespace.ExpandedName(None, 'mapInteractionTypeName')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 121, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mapInteraction._Automaton = _BuildAutomaton_11()




mapInteractions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'singleMapInteraction'), mapInteraction, scope=mapInteractions, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 129, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 129, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mapInteractions._UseForTag(pyxb.namespace.ExpandedName(None, 'singleMapInteraction')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 129, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mapInteractions._Automaton = _BuildAutomaton_12()




mapSearch._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'StarttimeStamp'), pyxb.binding.datatypes.dateTime, scope=mapSearch, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 138, 6)))

mapSearch._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'EndtimeStamp'), pyxb.binding.datatypes.dateTime, scope=mapSearch, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 139, 6)))

mapSearch._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'BBox'), bbox, scope=mapSearch, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 140, 6)))

mapSearch._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'textWithSuggestions'), textWithSuggestions, scope=mapSearch, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 141, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 140, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mapSearch._UseForTag(pyxb.namespace.ExpandedName(None, 'StarttimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 138, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mapSearch._UseForTag(pyxb.namespace.ExpandedName(None, 'EndtimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 139, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mapSearch._UseForTag(pyxb.namespace.ExpandedName(None, 'BBox')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 140, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mapSearch._UseForTag(pyxb.namespace.ExpandedName(None, 'textWithSuggestions')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 141, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mapSearch._Automaton = _BuildAutomaton_13()




mapSearchs._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mapSearchElement'), mapSearch, scope=mapSearchs, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 150, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 150, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mapSearchs._UseForTag(pyxb.namespace.ExpandedName(None, 'mapSearchElement')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 150, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mapSearchs._Automaton = _BuildAutomaton_14()




routing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'startRoutingInterfaceTimeStamp'), pyxb.binding.datatypes.dateTime, scope=routing, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 159, 5)))

routing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp'), pyxb.binding.datatypes.dateTime, scope=routing, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 160, 5)))

routing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'startRoutingTimeStamp'), pyxb.binding.datatypes.dateTime, scope=routing, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 161, 5)))

routing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'endRoutingTimeStamp'), pyxb.binding.datatypes.dateTime, scope=routing, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 162, 5)))

routing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OriginTextBoxHistory'), textWithSuggestions, scope=routing, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 163, 5)))

routing._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'DestiantionTextBoxHistory'), textWithSuggestions, scope=routing, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 164, 5)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 161, 5))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 162, 5))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(routing._UseForTag(pyxb.namespace.ExpandedName(None, 'startRoutingInterfaceTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 159, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(routing._UseForTag(pyxb.namespace.ExpandedName(None, 'endRoutingInterfaceSendRequestOrInterfaceClosedTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 160, 5))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(routing._UseForTag(pyxb.namespace.ExpandedName(None, 'startRoutingTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 161, 5))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(routing._UseForTag(pyxb.namespace.ExpandedName(None, 'endRoutingTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 162, 5))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(routing._UseForTag(pyxb.namespace.ExpandedName(None, 'OriginTextBoxHistory')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 163, 5))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(routing._UseForTag(pyxb.namespace.ExpandedName(None, 'DestiantionTextBoxHistory')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 164, 5))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
routing._Automaton = _BuildAutomaton_15()




routings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routingElement'), routing, scope=routings, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 173, 5)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 173, 5))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routings._UseForTag(pyxb.namespace.ExpandedName(None, 'routingElement')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 173, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
routings._Automaton = _BuildAutomaton_16()




spatialBookmark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'userPositionWithTimeStamp'), geocoordinateWithTimeStamp, scope=spatialBookmark, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 182, 6)))

spatialBookmark._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'notes'), pyxb.binding.datatypes.string, scope=spatialBookmark, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 183, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 183, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(spatialBookmark._UseForTag(pyxb.namespace.ExpandedName(None, 'userPositionWithTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 182, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(spatialBookmark._UseForTag(pyxb.namespace.ExpandedName(None, 'notes')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 183, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
spatialBookmark._Automaton = _BuildAutomaton_17()




spatialBookmarks._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'spatialBookmark'), spatialBookmark, scope=spatialBookmarks, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 193, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 193, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(spatialBookmarks._UseForTag(pyxb.namespace.ExpandedName(None, 'spatialBookmark')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 193, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
spatialBookmarks._Automaton = _BuildAutomaton_18()




MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'startApplicationTimeStamp'), pyxb.binding.datatypes.dateTime, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 203, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'endApplicationTimeStamp'), pyxb.binding.datatypes.dateTime, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 204, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'userPositionElements'), userPositions, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 205, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mapInteractionsElements'), mapInteractions, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 206, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mapSearchsElements'), mapSearchs, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 207, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routingsElements'), routings, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 208, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'questionsElements'), questions, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 209, 6)))

MappedSession._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'spatialBookmarksElements'), spatialBookmarks, scope=MappedSession, location=pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 210, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'startApplicationTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 203, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'endApplicationTimeStamp')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 204, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'userPositionElements')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 205, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'mapInteractionsElements')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 206, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'mapSearchsElements')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 207, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'routingsElements')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 208, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'questionsElements')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 209, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MappedSession._UseForTag(pyxb.namespace.ExpandedName(None, 'spatialBookmarksElements')), pyxb.utils.utility.Location('/home/sophie/repos/webGIS/xml-server/OuputDataSchema.xsd', 210, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
    ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
    ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
    ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MappedSession._Automaton = _BuildAutomaton_19()
