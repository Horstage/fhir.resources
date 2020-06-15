# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Encounter
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Encounter(domainresource.DomainResource):
    """ An interaction during which services are provided to the patient.
    An interaction between a patient and healthcare provider(s) for the purpose
    of providing healthcare service(s) or assessing the health status of a
    patient.
    """

    resource_type = Field("Encounter", const=True)

    account: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="account",
        title=(
            "List of `Reference` items referencing `Account` (represented as `dict`"
            " in JSON)"
        ),
        description="The set of accounts that may be used for billing for this Encounter",
    )

    appointment: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="appointment",
        title=(
            "List of `Reference` items referencing `Appointment` (represented as "
            "`dict` in JSON)"
        ),
        description="The appointment that scheduled this encounter",
    )

    basedOn: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="basedOn",
        title=(
            "List of `Reference` items referencing `ServiceRequest` (represented as"
            " `dict` in JSON)"
        ),
        description="The ServiceRequest that initiated this encounter",
    )

    classHistory: ListType[fhirtypes.EncounterClassHistoryType] = Field(
        None,
        alias="classHistory",
        title="List of `EncounterClassHistory` items (represented as `dict` in JSON)",
        description="List of past encounter classes",
    )

    class_fhir: fhirtypes.CodingType = Field(
        ...,
        alias="class",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="Classification of patient encounter",
    )

    diagnosis: ListType[fhirtypes.EncounterDiagnosisType] = Field(
        None,
        alias="diagnosis",
        title="List of `EncounterDiagnosis` items (represented as `dict` in JSON)",
        description="The list of diagnosis relevant to this encounter",
    )

    episodeOfCare: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="episodeOfCare",
        title=(
            "List of `Reference` items referencing `EpisodeOfCare` (represented as "
            "`dict` in JSON)"
        ),
        description="Episode(s) of care that this encounter should be recorded against",
    )

    hospitalization: fhirtypes.EncounterHospitalizationType = Field(
        None,
        alias="hospitalization",
        title="Type `EncounterHospitalization` (represented as `dict` in JSON)",
        description="Details about the admission to a healthcare service",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Identifier(s) by which this encounter is known",
    )

    length: fhirtypes.DurationType = Field(
        None,
        alias="length",
        title="Type `Duration` (represented as `dict` in JSON)",
        description="Quantity of time the encounter lasted (less time absent)",
    )

    location: ListType[fhirtypes.EncounterLocationType] = Field(
        None,
        alias="location",
        title="List of `EncounterLocation` items (represented as `dict` in JSON)",
        description="List of locations where the patient has been",
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title=(
            "Type `Reference` referencing `Encounter` (represented as `dict` in "
            "JSON)"
        ),
        description="Another Encounter this encounter is part of",
    )

    participant: ListType[fhirtypes.EncounterParticipantType] = Field(
        None,
        alias="participant",
        title="List of `EncounterParticipant` items (represented as `dict` in JSON)",
        description="List of participants involved in the encounter",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The start and end time of the encounter",
    )

    priority: fhirtypes.CodeableConceptType = Field(
        None,
        alias="priority",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Indicates the urgency of the encounter",
    )

    reasonCode: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="reasonCode",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Coded reason the encounter takes place",
    )

    reasonReference: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="reasonReference",
        title=(
            "List of `Reference` items referencing `Condition, Procedure, "
            "Observation, ImmunizationRecommendation` (represented as `dict` in "
            "JSON)"
        ),
        description="Reason the encounter takes place (reference)",
    )

    serviceProvider: fhirtypes.ReferenceType = Field(
        None,
        alias="serviceProvider",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="The organization (facility) responsible for this encounter",
    )

    serviceType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="serviceType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Specific type of service",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
    )

    statusHistory: ListType[fhirtypes.EncounterStatusHistoryType] = Field(
        None,
        alias="statusHistory",
        title="List of `EncounterStatusHistory` items (represented as `dict` in JSON)",
        description="List of past encounter statuses",
    )

    subject: fhirtypes.ReferenceType = Field(
        None,
        alias="subject",
        title=(
            "Type `Reference` referencing `Patient, Group` (represented as `dict` "
            "in JSON)"
        ),
        description="The patient or group present at the encounter",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Specific type of encounter",
    )


class EncounterClassHistory(backboneelement.BackboneElement):
    """ List of past encounter classes.
    The class history permits the tracking of the encounters transitions
    without needing to go  through the resource history.  This would be used
    for a case where an admission starts of as an emergency encounter, then
    transitions into an inpatient scenario. Doing this and not restarting a new
    encounter ensures that any lab/diagnostic results can more easily follow
    the patient and not require re-processing and not get lost or cancelled
    during a kind of discharge from emergency to inpatient.
    """

    resource_type = Field("EncounterClassHistory", const=True)

    class_fhir: fhirtypes.CodingType = Field(
        ...,
        alias="class",
        title="Type `Coding` (represented as `dict` in JSON)",
        description="inpatient | outpatient | ambulatory | emergency +",
    )

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The time that the episode was in the specified class",
    )


class EncounterDiagnosis(backboneelement.BackboneElement):
    """ The list of diagnosis relevant to this encounter.
    """

    resource_type = Field("EncounterDiagnosis", const=True)

    condition: fhirtypes.ReferenceType = Field(
        ...,
        alias="condition",
        title=(
            "Type `Reference` referencing `Condition, Procedure` (represented as "
            "`dict` in JSON)"
        ),
        description="The diagnosis or procedure relevant to the encounter",
    )

    rank: fhirtypes.PositiveInt = Field(
        None,
        alias="rank",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="Ranking of the diagnosis (for each role type)",
    )

    use: fhirtypes.CodeableConceptType = Field(
        None,
        alias="use",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "Role that this diagnosis has within the encounter (e.g. admission, "
            "billing, discharge \u2026)"
        ),
    )


class EncounterHospitalization(backboneelement.BackboneElement):
    """ Details about the admission to a healthcare service.
    """

    resource_type = Field("EncounterHospitalization", const=True)

    admitSource: fhirtypes.CodeableConceptType = Field(
        None,
        alias="admitSource",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="From where patient was admitted (physician referral, transfer)",
    )

    destination: fhirtypes.ReferenceType = Field(
        None,
        alias="destination",
        title=(
            "Type `Reference` referencing `Location, Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="Location/organization to which the patient is discharged",
    )

    dietPreference: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="dietPreference",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Diet preferences reported by the patient",
    )

    dischargeDisposition: fhirtypes.CodeableConceptType = Field(
        None,
        alias="dischargeDisposition",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="Category or kind of location after discharge",
    )

    origin: fhirtypes.ReferenceType = Field(
        None,
        alias="origin",
        title=(
            "Type `Reference` referencing `Location, Organization` (represented as "
            "`dict` in JSON)"
        ),
        description="The location/organization from which the patient came before admission",
    )

    preAdmissionIdentifier: fhirtypes.IdentifierType = Field(
        None,
        alias="preAdmissionIdentifier",
        title="Type `Identifier` (represented as `dict` in JSON)",
        description="Pre-admission identifier",
    )

    reAdmission: fhirtypes.CodeableConceptType = Field(
        None,
        alias="reAdmission",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The type of hospital re-admission that has occurred (if any). If the "
            "value is absent, then this is not identified as a readmission"
        ),
    )

    specialArrangement: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialArrangement",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Wheelchair, translator, stretcher, etc.",
    )

    specialCourtesy: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="specialCourtesy",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Special courtesies (VIP, board member)",
    )


class EncounterLocation(backboneelement.BackboneElement):
    """ List of locations where the patient has been.
    List of locations where  the patient has been during this encounter.
    """

    resource_type = Field("EncounterLocation", const=True)

    location: fhirtypes.ReferenceType = Field(
        ...,
        alias="location",
        title=(
            "Type `Reference` referencing `Location` (represented as `dict` in " "JSON)"
        ),
        description="Location the encounter takes place",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Time period during which the patient was present at the location",
    )

    physicalType: fhirtypes.CodeableConceptType = Field(
        None,
        alias="physicalType",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description=(
            "The physical type of the location (usually the level in the location "
            "hierachy - bed room ward etc.)"
        ),
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="planned | active | reserved | completed",
    )


class EncounterParticipant(backboneelement.BackboneElement):
    """ List of participants involved in the encounter.
    The list of people responsible for providing the service.
    """

    resource_type = Field("EncounterParticipant", const=True)

    individual: fhirtypes.ReferenceType = Field(
        None,
        alias="individual",
        title=(
            "Type `Reference` referencing `Practitioner, PractitionerRole, "
            "RelatedPerson` (represented as `dict` in JSON)"
        ),
        description="Persons involved in the encounter other than the patient",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Period of time during the encounter that the participant participated",
    )

    type: ListType[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title="List of `CodeableConcept` items (represented as `dict` in JSON)",
        description="Role of participant in encounter",
    )


class EncounterStatusHistory(backboneelement.BackboneElement):
    """ List of past encounter statuses.
    The status history permits the encounter resource to contain the status
    history without needing to read through the historical versions of the
    resource, or even have the server store them.
    """

    resource_type = Field("EncounterStatusHistory", const=True)

    period: fhirtypes.PeriodType = Field(
        ...,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="The time that the episode was in the specified status",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description=(
            "planned | arrived | triaged | in-progress | onleave | finished | "
            "cancelled +"
        ),
    )
