import unittest

from pypremis.premisrecord import *


class TestObjectMethods(unittest.TestCase):
    def testObject(self):
        a = PremisObject()

        a.set_objectIdentifier(1)
        a.get_objectIdentifier()
        a.add_objectIdentifier(1)

        a.set_objectCategory(1)
        a.get_objectCategory()

        a.set_preservationLevel(1)
        a.get_preservationLevel()
        a.add_preservationLevel(1)

        a.set_significantProperties(1)
        a.get_significantProperties()
        a.add_significantProperties(1)

        a.set_objectCharacteristics(1)
        a.get_objectCharacteristics()
        a.add_objectCharacteristics(1)

        a.set_originalName(1)
        a.get_originalName()

        a.set_storage(1)
        a.get_storage()
        a.add_storage(1)

        a.set_signatureInformation(1)
        a.get_signatureInformation()
        a.add_signatureInformation(1)

        a.set_environmentFunction(1)
        a.get_environmentFunction()
        a.add_environmentFunction(1)

        a.set_environmentDesignation(1)
        a.get_environmentDesignation()
        a.add_environmentDesignation(1)

        a.set_environmentRegistry(1)
        a.get_environmentRegistry()
        a.add_environmentRegistry(1)

        a.set_environmentExtension(1)
        a.get_environmentExtension()
        a.add_environmentExtension(1)

        a.set_relationship(1)
        a.get_relationship()
        a.add_relationship(1)

        a.set_linkingEventIdentifier(1)
        a.get_linkingEventIdentifier()
        a.add_linkingEventIdentifier(1)

        a.set_linkingRightsStatementIdentifier(1)
        a.get_linkingRightsStatementIdentifier()
        a.add_linkingRightsStatementIdentifier(1)

    def testObjectIdentifier(self):
        a = ObjectIdentifier()

        a.set_objectIdentifierType(1)
        a.get_objectIdentifierType()

        a.set_objectIdentifierValue(1)
        a.get_objectIdentifierValue()

    def testPreservationLevel(self):
        a = PreservationLevel()

        a.set_preservationLevelType(1)
        a.get_preservationLevelType()

        a.set_preservationLevelValue(1)
        a.get_preservationLevelValue()

        a.set_preservationLevelRole(1)
        a.get_preservationLevelRole()

        a.set_preservationLevelRationale(1)
        a.get_preservationLevelRationale()
        a.add_preservationLevelRationale(1)

        a.set_preservationLevelDateAssigned(1)
        a.get_preservationLevelDateAssigned()

    def testSignificantProperties(self):
        a = SignificantProperties()

        a.set_significantPropertiesType(1)
        a.get_significantPropertiesType()

        a.set_significantPropertiesValue(1)
        a.get_significantPropertiesValue()

        a.set_significantPropertiesExtension(1)
        a.get_significantPropertiesExtension()
        a.add_significantPropertiesExtension(1)

    def testObjectCharacteristics(self):
        a = ObjectCharacteristics()

        a.set_compositionLevel(1)
        a.get_compositionLevel()

        a.set_fixity(1)
        a.get_fixity()
        a.add_fixity(1)

        a.set_size(1)
        a.get_size()

        a.set_format(1)
        a.get_format()
        a.add_format(1)

        a.set_creatingApplication(1)
        a.get_creatingApplication()
        a.add_creatingApplication(1)

        a.set_inhibitors(1)
        a.get_inhibitors()
        a.add_inhibitors(1)

        a.set_objectCharacteristicsExtension(1)
        a.get_objectCharacteristicsExtension()
        a.add_objectCharacteristicsExtension(1)

    def testStorage(self):
        a = Storage()

        a.set_contentLocation(1)
        a.get_contentLocation()

        a.set_storageMedium(1)
        a.get_storageMedium()

    def testContentLocation(self):
        a = ContentLocation()

        a.set_contentLocationType(1)
        a.get_contentLocationType

        a.set_contentLocationValue(1)
        a.get_contentLocationValue()

    def testSignatureInformation(self):
        a = SignatureInformation()

        a.set_signature(1)
        a.get_signature()
        a.add_signature(1)

        a.set_signatureInformationExtension(1)
        a.get_signatureInformationExtension()
        a.add_signatureInformationExtension(1)

    def testSignature(self):
        a = Signature()

        a.set_signatureEncoding(1)
        a.get_signatureEncoding()

        a.set_signer(1)
        a.get_signer()

        a.set_signatureMethod(1)
        a.get_signatureMethod()

        a.set_signatureValue(1)
        a.get_signatureValue()

        a.set_signatureValidationRules(1)
        a.get_signatureValidationRules()

        a.set_signatureProperties(1)
        a.get_signatureProperties()
        a.add_signatureProperties(1)

        a.set_keyInformation(1)
        a.get_keyInformation()

    def testEnvironmentFunction(self):
        a = EnvironmentFunction()

        a.set_environmentFunctionType(1)
        a.get_environmentFunctionType()

        a.set_environmentFunctionLevel(1)
        a.get_environmentFunctionLevel()

    def testEnvironmentDesignation(self):
        a = EnvironmentDesignation()

        a.set_environmentName(1)
        a.get_environmentName()

        a.set_environmentVersion(1)
        a.get_environmentVersion()

        a.set_environmentOrigin(1)
        a.get_environmentOrigin()

        a.set_environmentDesignationNote(1)
        a.get_environmentDesignationNote()
        a.add_environmentDesignationNote(1)

        a.set_environmentDesignationExtension(1)
        a.get_environmentDesignationExtension()
        a.add_environmentDesignationExtension(1)

    def testEnvironmentRegistry(self):
        a = EnvironmentRegistry()

        a.set_environmentRegistryName(1)
        a.get_environmentRegistryName()

        a.set_environmentRegistryKey(1)
        a.get_environmentRegistryKey()

        a.set_environmentRegistryRole(1)
        a.get_environmentRegistryRole()

    def testRelationship(self):
        a = Relationship()

        a.set_relationshipType(1)
        a.get_relationshipType()

        a.set_relationshipSubType(1)
        a.get_relationshipSubType()

        a.set_relatedObjectIdentifier(1)
        a.get_relatedObjectIdentifier()
        a.add_relatedObjectIdentifier(1)

        a.set_relatedEventIdentifier(1)
        a.get_relatedEventIdentifier()
        a.add_relatedEventIdentifier(1)

        a.set_relatedEnvironmentPurpose(1)
        a.get_relatedEnvironmentPurpose()
        a.add_relatedEnvironmentPurpose(1)

        a.set_relatedEnvironmentCharacteristic(1)
        a.get_relatedEnvironmentCharacteristic()

    def testLinkingEventIdentifier(self):
        a = LinkingEventIdentifier()

        a.set_linkingEventIdentifierType(1)
        a.get_linkingEventIdentifierType()

        a.set_linkingEventIdentifierValue(1)
        a.get_linkingEventIdentifierValue()

    def testLinkingRightsStatementIdentifier(self):
        a = LinkingRightsStatementIdentifier()

        a.set_linkingRightsStatementIdentifierType(1)
        a.get_linkingRightsStatementIdentifierType()

        a.set_linkingRightsStatementIdentifierValue(1)
        a.get_linkingRightsStatementIdentifierValue()

    def testRelatedEventIdentifier(self):
        a = RelatedEventIdentifier()

        a.set_relatedEventIdentifierType(1)
        a.get_relatedEventIdentifierType()

        a.set_relatedEventIdentifierValue(1)
        a.get_relatedEventIdentifierValue()

        a.set_relatedEventSequence(1)
        a.get_relatedEventSequence()

    def testRelatedObjectIdentifier(self):
        a = RelatedObjectIdentifier()

        a.set_relatedObjectIdentifierType(1)
        a.get_relatedObjectIdentifierType()

        a.set_relatedObjectIdentifierValue(1)
        a.get_relatedObjectIdentifierValue()

        a.set_relatedObjectSequence(1)
        a.get_relatedObjectSequence()

    def testInhibitors(self):
        a = Inhibitors()

        a.set_inhibitorType(1)
        a.get_inhibitorType()

        a.set_inhibitorTarget(1)
        a.get_inhibitorTarget()
        a.add_inhibitorTarget(1)

        a.set_inhibitorKey(1)
        a.get_inhibitorKey()

    def testCreatingApplication(self):
        a = CreatingApplication()

        a.set_creatingApplicationName(1)
        a.get_creatingApplicationName()

        a.set_creatingApplicationVersion(1)
        a.get_creatingApplicationVersion()

        a.set_dateCreatedByApplication(1)
        a.get_dateCreatedByApplication()

        a.set_creatingApplicationExtension(1)
        a.get_creatingApplicationExtension()
        a.add_creatingApplicationExtension(1)

    def testFormat(self):
        a = Format()

        a.set_formatDesignation(1)
        a.get_formatDesignation()

        a.set_formatRegistry(1)
        a.get_formatRegistry()

        a.set_formatNote(1)
        a.get_formatNote()
        a.add_formatNote(1)

    def testFormatDesignation(self):
        a = FormatDesignation()

        a.set_formatName(1)
        a.get_formatName()

        a.set_formatVersion(1)
        a.get_formatVersion()

    def testFormatRegistry(self):
        a = FormatRegistry()

        a.set_formatRegistryName(1)
        a.get_formatRegistryName()

        a.set_formatRegistryKey(1)
        a.get_formatRegistryKey()

        a.set_formatRegistryRole(1)
        a.get_formatRegistryRole()

    def testFixity(self):
        a = Fixity()

        a.set_messageDigestAlgorithm(1)
        a.get_messageDigestAlgorithm()

        a.set_messageDigest(1)
        a.get_messageDigest()

        a.set_messageDigestOriginator(1)
        a.get_messageDigestOriginator()


class TestAgentMethods(unittest.TestCase):
    def testAgent(self):
        a = PremisAgent()

        a.set_agentIdentifier(1)
        a.get_agentIdentifier()
        a.add_agentIdentifier(1)

        a.set_agentName(1)
        a.get_agentName()
        a.add_agentName(1)

        a.set_agentType(1)
        a.get_agentType()

        a.set_agentVersion(1)
        a.get_agentVersion()

        a.set_agentNote(1)
        a.get_agentNote()
        a.add_agentNote(1)

        a.set_agentExtension(1)
        a.get_agentExtension()
        a.add_agentExtension(1)

        a.set_linkingEventIdentifier(1)
        a.get_linkingEventIdentifier()
        a.add_linkingEventIdentifier(1)

        a.set_linkingRightsStatementIdentifier(1)
        a.get_linkingRightsStatementIdentifier()
        a.add_linkingRightsStatementIdentifier(1)

        a.set_linkingEnvironmentIdentifier(1)
        a.get_linkingEnvironmentIdentifier()
        a.add_linkingEnvironmentIdentifier(1)

    def testAgentIdentifier(self):
        a = AgentIdentifier()

        a.set_agentIdentifierType(1)
        a.get_agentIdentifierType()

        a.set_agentIdentifierValue(1)
        a.get_agentIdentifierValue()

    def testLinkingEnvironmentIdentifier(self):
        a = LinkingEnvironmentIdentifier()

        a.set_linkingEnvironmentIdentifierType(1)
        a.get_linkingEnvironmentIdentifierType()

        a.set_linkingEnvironmentIdentifierValue(1)
        a.get_linkingEnvironmentIdentifierValue()

        a.set_linkingEnvironmentRole(1)
        a.get_linkingEnvironmentRole()
        a.add_linkingEnvironmentRole(1)


class TestEvent(unittest.TestCase):
    def testEvent(self):
        a = PremisEvent()

        a.set_eventIdentifier(1)
        a.get_eventIdentifier()

        a.set_eventType(1)
        a.get_eventType()

        a.set_eventDateTime(1)
        a.get_eventDateTime()

        a.set_eventDetailInformation(1)
        a.get_eventDetailInformation()
        a.add_eventDetailInformation(1)

        a.set_eventOutcomeInformation(1)
        a.get_eventOutcomeInformation()
        a.add_eventOutcomeInformation(1)

        a.set_linkingAgentIdentifier(1)
        a.get_linkingAgentIdentifier()
        a.add_linkingAgentIdentifier(1)

        a.set_linkingObjectIdentifier(1)
        a.get_linkingObjectIdentifier()
        a.add_linkingObjectIdentifier(1)

    def testEventIdentifier(self):
        a = EventIdentifier()

        a.set_eventIdentifierType(1)
        a.get_eventIdentifierType()

        a.set_eventIdentifierValue(1)
        a.get_eventIdentifierValue()

    def testEventDetailInformation(self):
        a = EventDetailInformation()

        a.set_eventDetail(1)
        a.get_eventDetail()

        a.set_eventDetailExtension(1)
        a.get_eventDetailExtension()
        a.add_eventDetailExtension(1)

    def testEventOutcomeInformation(self):
        a = EventOutcomeInformation()

        a.set_eventOutcome(1)
        a.get_eventOutcome()

        a.set_eventOutcomeDetail(1)
        a.get_eventOutcomeDetail()
        a.add_eventOutcomeDetail(1)

    def testEventOutcomeDetail(self):
        a = EventOutcomeDetail()

        a.set_eventOutcomeDetailNote(1)
        a.get_eventOutcomeDetailNote()

        a.set_eventOutcomeDetailExtension(1)
        a.get_eventOutcomeDetailExtension()
        a.add_eventOutcomeDetailExtension(1)

    def testLinkingAgentIdentifier(self):
        a = LinkingAgentIdentifier()

        a.set_linkingAgentIdentifierType(1)
        a.get_linkingAgentIdentifierType()

        a.set_linkingAgentIdentifierValue(1)
        a.get_linkingAgentIdentifierValue()

        a.set_linkingAgentRole(1)
        a.get_linkingAgentRole()
        a.add_linkingAgentRole(1)

    def testLinkingObjectIdentifier(self):
        a = LinkingObjectIdentifier()

        a.set_linkingObjectIdentifierType(1)
        a.get_linkingObjectIdentifierType()

        a.set_linkingObjectIdentifierValue(1)
        a.get_linkingObjectIdentifierValue()

        a.set_linkingObjectRole(1)
        a.get_linkingObjectRole()
        a.add_linkingObjectRole(1)


class TestRights(unittest.TestCase):
    def testRights(self):
        a = PremisRights()

        a.set_rightsStatement(1)
        a.get_rightsStatement()
        a.add_rightsStatement(1)

        a.set_rightsExtension(1)
        a.get_rightsExtension()
        a.add_rightsExtension(1)

    def testRightsStatement(self):
        a = RightsStatement()

        a.set_rightsStatementIdentifier(1)
        a.get_rightsStatementIdentifier()

        a.set_rightsBasis(1)
        a.get_rightsBasis()

        a.set_copyrightInformation(1)
        a.get_copyrightInformation()

        a.set_licenseInformation(1)
        a.get_licenseInformation()

        a.set_statuteInformation(1)
        a.get_statuteInformation()
        a.add_statuteInformation(1)

        a.set_otherRightsInformation(1)
        a.get_otherRightsInformation()

        a.set_rightsGranted(1)
        a.get_rightsGranted()
        a.add_rightsGranted(1)

        a.set_linkingObjectIdentifier(1)
        a.get_linkingObjectIdentifier()
        a.add_linkingObjectIdentifier(1)

        a.set_linkingAgentIdentifier(1)
        a.get_linkingAgentIdentifier()
        a.add_linkingAgentIdentifier(1)

    def testRightsStatementIdentifier(self):
        a = RightsStatementIdentifier()

        a.set_rightsStatementIdentifierType(1)
        a.get_rightsStatementIdentifierType()

        a.set_rightsStatementIdentifierValue(1)
        a.get_rightsStatementIdentifierValue()

    def testCopyrightInformation(self):
        a = CopyrightInformation()

        a.set_copyrightStatus(1)
        a.get_copyrightStatus()

        a.set_copyrightJurisdiction(1)
        a.get_copyrightJurisdiction()

        a.set_copyrightStatusDeterminationDate(1)
        a.get_copyrightStatusDeterminationDate()

        a.set_copyrightNote(1)
        a.get_copyrightNote()
        a.add_copyrightNote(1)

        a.set_copyrightDocumentationIdentifier(1)
        a.get_copyrightDocumentationIdentifier()
        a.add_copyrightDocumentationIdentifier(1)

        a.set_copyrightApplicableDates(1)
        a.get_copyrightApplicableDates()

    def testCopyrightApplicableDates(self):
        a = CopyrightApplicableDates()

        a.set_startDate(1)
        a.get_startDate()

        a.set_endDate(1)
        a.get_endDate()

    def testCopyrightDocumentationIdentifer(self):
        a = CopyrightDocumentationIdentifier()

        a.set_copyrightDocumentationIdentifierType(1)
        a.get_copyrightDocumentationIdentifierType()

        a.set_copyrightDocumentationIdentifierValue(1)
        a.get_copyrightDocumentationIdentifierValue()

        a.set_copyrightDocumentationRole(1)
        a.get_copyrightDocumentationRole()

    def testLicenseInformation(self):
        a = LicenseInformation()

        a.set_licenseDocumentationIdentifier(1)
        a.get_licenseDocumentationIdentifier()
        a.add_licenseDocumentationIdentifier(1)

        a.set_licenseTerms(1)
        a.get_licenseTerms()

        a.set_licenseNote(1)
        a.get_licenseNote()
        a.add_licenseNote(1)

        a.set_licenseApplicableDates(1)
        a.get_licenseApplicableDates()

    def testLicenseApplicableDates(self):
        a = LicenseApplicableDates()

        a.set_startDate(1)
        a.get_startDate()

        a.set_endDate(1)
        a.get_endDate()

    def testLicenseDocumentationIdentifier(self):
        a = LicenseDocumentationIdentifier()

        a.set_licenseDocumentationIdentifierType(1)
        a.get_licenseDocumentationIdentifierType()

        a.set_licenseDocumentationIdentifierValue(1)
        a.get_licenseDocumentationIdentifierValue()

        a.set_licenseDocumentationRole(1)
        a.get_licenseDocumentationRole()

    def testStatuteInformation(self):
        a = StatuteInformation()

        a.set_statuteJurisdiction(1)
        a.get_statuteJurisdiction()

        a.set_statuteCitation(1)
        a.get_statuteCitation()

        a.set_statuteInformationDeterminationDate(1)
        a.get_statuteInformationDeterminationDate()

        a.set_statuteNote(1)
        a.get_statuteNote()
        a.add_statuteNote(1)

        a.set_statuteDocumentationIdentifier(1)
        a.get_statuteDocumentationIdentifier()
        a.add_statuteDocumentationIdentifier(1)

        a.set_statuteApplicableDates(1)
        a.get_statuteApplicableDates()

    def testStatuteApplicableDates(self):
        a = StatuteApplicableDates()

        a.set_startDate(1)
        a.get_startDate()

        a.set_endDate(1)
        a.get_endDate()

    def testStatuteDocumentationIdentifier(self):
        a = StatuteDocumentationIdentifier()

        a.set_statuteDocumentationIdentifierType(1)
        a.get_statuteDocumentationIdentifierType()

        a.set_statuteDocumentationIdentifierValue(1)
        a.get_statuteDocumentationIdentifierValue()

        a.set_statuteDocumentationRole(1)
        a.get_statuteDocumentationRole()

    def testOtherRightsInformation(self):
        a = OtherRightsInformation()

        a.set_otherRightsDocumentationIdentifier(1)
        a.get_otherRightsDocumentationIdentifier()
        a.add_otherRightsDocumentationIdentifier(1)

        a.set_otherRightsBasis(1)
        a.get_otherRightsBasis()

        a.set_otherRightsApplicableDates(1)
        a.get_otherRightsApplicableDates()

        a.set_otherRightsNote(1)
        a.get_otherRightsNote()
        a.add_otherRightsNote(1)

    def testOtherRightsApplicableDates(self):
        a = OtherRightsApplicableDates()

        a.set_startDate(1)
        a.get_startDate()

        a.set_endDate(1)
        a.get_endDate()

    def testOtherRightsDocumentationIdentifier(self):
        a = OtherRightsDocumentationIdentifier()

        a.set_otherRightsDocumentationIdentifierType(1)
        a.get_otherRightsDocumentationIdentifierType()

        a.set_otherRightsDocumentationIdentifierValue(1)
        a.get_otherRightsDocumentationIdentifierValue()

        a.set_otherRightsDocumentationRole(1)
        a.get_otherRightsDocumentationRole()

    def testRightsGranted(self):
        a = RightsGranted()

        a.set_act(1)
        a.get_act()

        a.set_restriction(1)
        a.get_restriction()
        a.add_restriction(1)

        a.set_termOfGrant(1)
        a.get_termOfGrant()

        a.set_termOfRestriction(1)
        a.get_termOfRestriction()

        a.set_rightsGrantedNote(1)
        a.get_rightsGrantedNote()
        a.add_rightsGrantedNote(1)

    def testTermOfRestriction(self):
        a = TermOfRestriction()

        a.set_startDate(1)
        a.get_startDate()

        a.set_endDate(1)
        a.get_endDate()

    def testTermOfGrant(self):
        a = TermOfGrant()

        a.set_startDate(1)
        a.get_startDate()

        a.set_endDate(1)
        a.get_endDate()


if __name__ == '__main__':
    unittest.main()
