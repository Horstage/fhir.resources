# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""
from typing import List as ListType

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.
    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """

    resource_type = Field("Account", const=True)

    coverage: ListType[fhirtypes.AccountCoverageType] = Field(
        None,
        alias="coverage",
        title="List of `AccountCoverage` items (represented as `dict` in JSON)",
        description=(
            "The party(s) that are responsible for covering the payment of this "
            "account, and what order should they be applied to the account"
        ),
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title="Type `String` (represented as `dict` in JSON)",
        description="Explanation of purpose/use",
    )

    guarantor: ListType[fhirtypes.AccountGuarantorType] = Field(
        None,
        alias="guarantor",
        title="List of `AccountGuarantor` items (represented as `dict` in JSON)",
        description="The parties ultimately responsible for balancing the Account",
    )

    identifier: ListType[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="List of `Identifier` items (represented as `dict` in JSON)",
        description="Account number",
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="Type `String` (represented as `dict` in JSON)",
        description="Human-readable label",
    )

    owner: fhirtypes.ReferenceType = Field(
        None,
        alias="owner",
        title=(
            "Type `Reference` referencing `Organization` (represented as `dict` in "
            "JSON)"
        ),
        description="Entity managing the Account",
    )

    partOf: fhirtypes.ReferenceType = Field(
        None,
        alias="partOf",
        title="Type `Reference` referencing `Account` (represented as `dict` in JSON)",
        description="Reference to a parent Account",
    )

    servicePeriod: fhirtypes.PeriodType = Field(
        None,
        alias="servicePeriod",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Transaction window",
    )

    status: fhirtypes.Code = Field(
        ...,
        alias="status",
        title="Type `Code` (represented as `dict` in JSON)",
        description="active | inactive | entered-in-error | on-hold | unknown",
    )

    subject: ListType[fhirtypes.ReferenceType] = Field(
        None,
        alias="subject",
        title=(
            "List of `Reference` items referencing `Patient, Device, Practitioner, "
            "PractitionerRole, Location, HealthcareService, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="The entity that caused the expenses",
    )

    type: fhirtypes.CodeableConceptType = Field(
        None,
        alias="type",
        title="Type `CodeableConcept` (represented as `dict` in JSON)",
        description="E.g. patient, expense, depreciation",
    )


class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """

    resource_type = Field("AccountCoverage", const=True)

    coverage: fhirtypes.ReferenceType = Field(
        ...,
        alias="coverage",
        title=(
            "Type `Reference` referencing `Coverage` (represented as `dict` in " "JSON)"
        ),
        description=(
            "The party(s), such as insurances, that may contribute to the payment "
            "of this account"
        ),
    )

    priority: fhirtypes.PositiveInt = Field(
        None,
        alias="priority",
        title="Type `PositiveInt` (represented as `dict` in JSON)",
        description="The priority of the coverage in the context of this account",
    )


class AccountGuarantor(backboneelement.BackboneElement):
    """ The parties ultimately responsible for balancing the Account.
    The parties responsible for balancing the account if other payment options
    fall short.
    """

    resource_type = Field("AccountGuarantor", const=True)

    onHold: bool = Field(
        None,
        alias="onHold",
        title="Type `bool`",
        description="Credit or other hold applied",
    )

    party: fhirtypes.ReferenceType = Field(
        ...,
        alias="party",
        title=(
            "Type `Reference` referencing `Patient, RelatedPerson, Organization` "
            "(represented as `dict` in JSON)"
        ),
        description="Responsible entity",
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Type `Period` (represented as `dict` in JSON)",
        description="Guarantee account during",
    )
