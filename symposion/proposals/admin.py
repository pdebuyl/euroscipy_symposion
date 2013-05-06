from django.contrib import admin

from symposion.proposals.actions import export_as_csv_action
from symposion.proposals.models import ProposalSection, ProposalKind, ProposalBase


admin.site.register(ProposalBase,
    list_display = [
        "id",
        "title",
        "speaker",
        "speaker_email",
        "kind",
        "cancelled",
    ],
    list_filter = [
        "kind__name",
        "result__accepted",
    ],
    actions = [export_as_csv_action("CSV Export", fields=[
        "id",
        "title",
        "speaker",
        "speaker_email",
        "kind",
    ])]
)


admin.site.register(ProposalSection)
admin.site.register(ProposalKind)
