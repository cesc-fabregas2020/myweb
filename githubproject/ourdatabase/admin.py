from django.contrib import admin
from ourdatabase.models import *
# Register your models here.
class ActionTypeAdmin(admin.ModelAdmin):
    pass

class ActivitiesAdmin(admin.ModelAdmin):
    raw_id_fields = ('assay','doc','record','molregno','data_validity_comment','bao_endpoint','src',)

class ActivityPropertiesAdmin(admin.ModelAdmin):
    raw_id_fields = ('activity',)
    search_fields = ('type',)

class ActivitySmidAdmin(admin.ModelAdmin):
    pass

class ActivityStdsLookupAdmin(admin.ModelAdmin):
    search_fields = ('standard_type',)

class ActivitySuppAdim(admin.ModelAdmin):
    raw_id_fields = ('smid',)

class ActivitySuppMapAdmin(admin.ModelAdmin):
    raw_id_fields = ('activity','smid',)

class AssayClassMapAdmin(admin.ModelAdmin):
    raw_id_fields = ('assay','assay_class',)

class AssayClassificationAdmin(admin.ModelAdmin):
    pass

class AssayParametersAdmin(admin.ModelAdmin):
    raw_id_fields = ('assay',)

class AssayTypeAdmin(admin.ModelAdmin):
    pass

class AssaysAdmin(admin.ModelAdmin):
    raw_id_fields = ('doc','assay_type','tid','relationship_type','confidence_score','curated_by','src','cell','bao_format','tissue','variant',)

class AtcClassificationAdmin(admin.ModelAdmin):
    pass

class AuthGroupAdmin(admin.ModelAdmin):
    pass

class AuthGroupPermissionsAdmin(admin.ModelAdmin):
    raw_id_fields = ('group','permission',)

class AuthPermissionAdmin(admin.ModelAdmin):
    raw_id_fields = ('content_type',)

class AuthUserAdmin(admin.ModelAdmin):
    pass

class AuthUserGroupsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user','group',)

class AuthUserUserPermissionsAdmin(admin.ModelAdmin):
    raw_id_fields = ('user','permission',)

class BindingSitesAdmin(admin.ModelAdmin):
    raw_id_fields = ('tid',)

class BioComponentSequencesAdmin(admin.ModelAdmin):
    pass

class BioassayOntologyAdmin(admin.ModelAdmin):
    pass

class BiotherapeuticComponentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno','component',)

class BiotherapeuticsAdmin(admin.ModelAdmin):
    pass

class CellDictionaryAdmin(admin.ModelAdmin):
    pass

class ChemblIdLookupAdmin(admin.ModelAdmin):
    search_fields = ('chembl_id','entity_type','entity_id','status',)

class ComponentClassAdmin(admin.ModelAdmin):
    raw_id_fields = ('component','protein_class',)

class ComponentDomainsAdmin(admin.ModelAdmin):
    raw_id_fields = ('domain','component',)

class ComponentGoAdmin(admin.ModelAdmin):
    raw_id_fields = ('component','go',)

class ComponentSequencesAdmin(admin.ModelAdmin):
    pass

class ComponentSynonymsAdmin(admin.ModelAdmin):
    raw_id_fields = ('component',)

class CompoundPropertiesAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno',)

class CompoundRecordsAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno','doc','src',)

class CompoundStructuralAlertsAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno','alert',)

class CompoundStructuresAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno',)

class ConfidenceScoreLookupAdmin(admin.ModelAdmin):
    pass

class CurationLookupAdmin(admin.ModelAdmin):
    pass

class DataValidityLookupAdmin(admin.ModelAdmin):
    pass

class DefinedDailyDoseAdmin(admin.ModelAdmin):
    raw_id_fields = ('atc_code',)

class DjangoAdminLogAdmin(admin.ModelAdmin):
    pass

class DjangoContentTypeAdmin(admin.ModelAdmin):
    pass

class DjangoMigrationsAdmin(admin.ModelAdmin):
    pass

class DjangoSessionAdmin(admin.ModelAdmin):
    pass

class DocsAdmin(admin.ModelAdmin):
    raw_id_fields = ('chembl',)

class DomainsAdmin(admin.ModelAdmin):
    pass

class DrugIndicationAdmin(admin.ModelAdmin):
    raw_id_fields = ('record','molregno',)

class DrugMechanismAdmin(admin.ModelAdmin):
    raw_id_fields = ('record','molregno','tid','site','action_type')

class FormulationsAdmin(admin.ModelAdmin):
    raw_id_fields = ('product','record','molregno',)

class FracClassificationAdmin(admin.ModelAdmin):
    pass

class GoClassificationAdmin(admin.ModelAdmin):
    pass

class HracClassificationAdmin(admin.ModelAdmin):
    pass

class IndicationRefsAdmin(admin.ModelAdmin):
    raw_id_fields = ('drugind',)

class IracClassificationAdmin(admin.ModelAdmin):
    pass

class LigandEffAdmin(admin.ModelAdmin):
    raw_id_fields = ('activity',)

class MechanismRefsAdmin(admin.ModelAdmin):
    raw_id_fields = ('mec',)

class MetabolismAdmin(admin.ModelAdmin):
    raw_id_fields = ('drug_record','substrate_record','metabolite_record',)

class MetabolismRefsAdmin(admin.ModelAdmin):
    raw_id_fields = ('met',)

class MoleculeAtcClassificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('level5','molregno',)

class MoleculeDictionaryAdmin(admin.ModelAdmin):
    raw_id_fields = ('chembl',)

class MoleculeFracClassificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('frac_class','molregno',)

class MoleculeHierarchyAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno','parent_molregno','active_molregno',)

class MoleculeHracClassificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('hrac_class','molregno',)

class MoleculeIracClassificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('irac_class','molregno',)

class MoleculeSynonymsAdmin(admin.ModelAdmin):
    raw_id_fields = ('molregno','res_stem',)

class OrganismClassAdmin(admin.ModelAdmin):
    pass

class PatentUseCodesAdmin(admin.ModelAdmin):
    pass

class PredictedBindingDomainsAdmin(admin.ModelAdmin):
    raw_id_fields = ('activity','site',)

class ProductPatentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('product','patent_use_code',)

class ProductsAdmin(admin.ModelAdmin):
    pass

class ProteinClassSynonymsAdmin(admin.ModelAdmin):
    raw_id_fields = ('protein_class',)

class ProteinClassificationAdmin(admin.ModelAdmin):
    pass

class ProteinFamilyClassificationAdmin(admin.ModelAdmin):
    pass

class RelationshipTypeAdmin(admin.ModelAdmin):
    pass

class ResearchCompaniesAdmin(admin.ModelAdmin):
    raw_id_fields = ('res_stem',)

class ResearchStemAdmin(admin.ModelAdmin):
    pass

class SiteComponentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('site','component','domain',)

class SourceAdmin(admin.ModelAdmin):
    pass

class StructuralAlertSetsAdmin(admin.ModelAdmin):
    pass

class StructuralAlertsAdmin(admin.ModelAdmin):
    raw_id_fields = ('alert_set',)

class TargetComponentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('tid','component',)

class TargetDictionaryAdmin(admin.ModelAdmin):
    raw_id_fields = ('target_type','chembl',)

class TargetRelationsAdmin(admin.ModelAdmin):
    raw_id_fields = ('tid','related_tid',)

class TargetTypeAdmin(admin.ModelAdmin):
    pass

class TissueDictionaryAdmin(admin.ModelAdmin):
    raw_id_fields = ('chembl',)

class UsanStemsAdmin(admin.ModelAdmin):
    pass

class VariantSequencesAdmin(admin.ModelAdmin):
    pass

class VersionAdmin(admin.ModelAdmin):
    pass

class HumankinaseAdmin(admin.ModelAdmin):
    raw_id_fields = ('chemblid',)

class OsrimoleculeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ActionType,ActionTypeAdmin)
admin.site.register(Activities,ActivitiesAdmin)
admin.site.register(ActivityProperties,ActivityPropertiesAdmin)
admin.site.register(ActivitySmid,ActivitySmidAdmin)
admin.site.register(ActivityStdsLookup,ActivityStdsLookupAdmin)
admin.site.register(ActivitySupp,ActivitySuppAdim)
admin.site.register(ActivitySuppMap,ActivitySuppMapAdmin)
admin.site.register(AssayClassMap,AssayClassMapAdmin)
admin.site.register(AssayClassification,AssayClassificationAdmin)
admin.site.register(AssayParameters,AssayParametersAdmin)
admin.site.register(AssayType,AssayTypeAdmin)
admin.site.register(Assays,AssaysAdmin)
admin.site.register(AtcClassification,AtcClassificationAdmin)
admin.site.register(AuthGroup,AuthGroupAdmin)
admin.site.register(AuthGroupPermissions,AuthGroupPermissionsAdmin)
admin.site.register(AuthPermission,AuthPermissionAdmin)
admin.site.register(AuthUser,AuthUserAdmin)
admin.site.register(AuthUserGroups,AuthUserGroupsAdmin)
admin.site.register(AuthUserUserPermissions,AuthUserUserPermissionsAdmin)
admin.site.register(BindingSites,BindingSitesAdmin)
admin.site.register(BioComponentSequences,BioComponentSequencesAdmin)
admin.site.register(BioassayOntology,BioassayOntologyAdmin)
admin.site.register(BiotherapeuticComponents,BiotherapeuticComponentsAdmin)
admin.site.register(Biotherapeutics,BiotherapeuticsAdmin)
admin.site.register(CellDictionary,CellDictionaryAdmin)
admin.site.register(ChemblIdLookup,ChemblIdLookupAdmin)
admin.site.register(ComponentClass,ComponentClassAdmin)
admin.site.register(ComponentDomains,ComponentDomainsAdmin)
admin.site.register(ComponentGo,ComponentGoAdmin)
admin.site.register(ComponentSequences,ComponentSequencesAdmin)
admin.site.register(ComponentSynonyms,ComponentSynonymsAdmin)
admin.site.register(CompoundProperties,CompoundPropertiesAdmin)
admin.site.register(CompoundRecords,CompoundRecordsAdmin)
admin.site.register(CompoundStructuralAlerts,CompoundStructuralAlertsAdmin)
admin.site.register(CompoundStructures,CompoundStructuresAdmin)
admin.site.register(ConfidenceScoreLookup,ConfidenceScoreLookupAdmin)
admin.site.register(CurationLookup,CurationLookupAdmin)
admin.site.register(DataValidityLookup,DataValidityLookupAdmin)
admin.site.register(DefinedDailyDose,DefinedDailyDoseAdmin)
admin.site.register(DjangoAdminLog,DjangoAdminLogAdmin)
admin.site.register(DjangoContentType,DjangoContentTypeAdmin)
admin.site.register(DjangoMigrations,DjangoMigrationsAdmin)
admin.site.register(DjangoSession,DjangoSessionAdmin)
admin.site.register(Docs,DocsAdmin)
admin.site.register(Domains,DomainsAdmin)
admin.site.register(DrugIndication,DrugIndicationAdmin)
admin.site.register(DrugMechanism,DrugMechanismAdmin)
admin.site.register(Formulations,FormulationsAdmin)
admin.site.register(FracClassification,FracClassificationAdmin)
admin.site.register(GoClassification,GoClassificationAdmin)
admin.site.register(HracClassification,HracClassificationAdmin)
admin.site.register(IndicationRefs,IndicationRefsAdmin)
admin.site.register(IracClassification,IracClassificationAdmin)
admin.site.register(LigandEff,LigandEffAdmin)
admin.site.register(MechanismRefs,MechanismRefsAdmin)
admin.site.register(Metabolism,MetabolismAdmin)
admin.site.register(MetabolismRefs,MetabolismRefsAdmin)
admin.site.register(MoleculeAtcClassification,MoleculeAtcClassificationAdmin)
admin.site.register(MoleculeDictionary,MoleculeDictionaryAdmin)
admin.site.register(MoleculeFracClassification,MoleculeFracClassificationAdmin)
admin.site.register(MoleculeHierarchy,MoleculeHierarchyAdmin)
admin.site.register(MoleculeHracClassification,MoleculeHracClassificationAdmin)
admin.site.register(MoleculeIracClassification,MoleculeIracClassificationAdmin)
admin.site.register(MoleculeSynonyms,MoleculeSynonymsAdmin)
admin.site.register(OrganismClass,OrganismClassAdmin)
admin.site.register(PatentUseCodes,PatentUseCodesAdmin)
admin.site.register(PredictedBindingDomains,PredictedBindingDomainsAdmin)
admin.site.register(ProductPatents,ProductPatentsAdmin)
admin.site.register(Products,ProductsAdmin)
admin.site.register(ProteinClassSynonyms,ProteinClassSynonymsAdmin)
admin.site.register(ProteinClassification,ProteinClassificationAdmin)
admin.site.register(ProteinFamilyClassification,ProteinFamilyClassificationAdmin)
admin.site.register(RelationshipType,RelationshipTypeAdmin)
admin.site.register(ResearchCompanies,ResearchCompaniesAdmin)
admin.site.register(ResearchStem,ResearchStemAdmin)
admin.site.register(SiteComponents,SiteComponentsAdmin)
admin.site.register(Source,SourceAdmin)
admin.site.register(StructuralAlerts,StructuralAlertsAdmin)
admin.site.register(StructuralAlertSets,StructuralAlertSetsAdmin)
admin.site.register(TargetComponents,TargetComponentsAdmin)
admin.site.register(TargetDictionary,TargetDictionaryAdmin)
admin.site.register(TargetRelations,TargetRelationsAdmin)
admin.site.register(TargetType,TargetTypeAdmin)
admin.site.register(TissueDictionary,TissueDictionaryAdmin)
admin.site.register(UsanStems,UsanStemsAdmin)
admin.site.register(VariantSequences,VariantSequencesAdmin)
admin.site.register(Version,VersionAdmin)
admin.site.register(Humankinase,HumankinaseAdmin)
admin.site.register(Osrimolecule,OsrimoleculeAdmin)