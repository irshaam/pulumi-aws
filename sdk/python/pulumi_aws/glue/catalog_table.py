# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['CatalogTable']


class CatalogTable(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CatalogTablePartitionKeyArgs']]]]] = None,
                 retention: Optional[pulumi.Input[int]] = None,
                 storage_descriptor: Optional[pulumi.Input[pulumi.InputType['CatalogTableStorageDescriptorArgs']]] = None,
                 table_type: Optional[pulumi.Input[str]] = None,
                 view_expanded_text: Optional[pulumi.Input[str]] = None,
                 view_original_text: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Glue Catalog Table Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality.

        ## Example Usage
        ### Basic Table

        ```python
        import pulumi
        import pulumi_aws as aws

        aws_glue_catalog_table = aws.glue.CatalogTable("awsGlueCatalogTable",
            database_name="MyCatalogDatabase",
            name="MyCatalogTable")
        ```
        ### Parquet Table for Athena

        ```python
        import pulumi
        import pulumi_aws as aws

        aws_glue_catalog_table = aws.glue.CatalogTable("awsGlueCatalogTable",
            database_name="MyCatalogDatabase",
            name="MyCatalogTable",
            parameters={
                "EXTERNAL": "TRUE",
                "parquet.compression": "SNAPPY",
            },
            storage_descriptor=aws.glue.CatalogTableStorageDescriptorArgs(
                columns=[
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        name="my_string",
                        type="string",
                    ),
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        name="my_double",
                        type="double",
                    ),
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        comment="",
                        name="my_date",
                        type="date",
                    ),
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        comment="",
                        name="my_bigint",
                        type="bigint",
                    ),
                    aws.glue.CatalogTableStorageDescriptorColumnArgs(
                        comment="",
                        name="my_struct",
                        type="struct<my_nested_string:string>",
                    ),
                ],
                input_format="org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
                location="s3://my-bucket/event-streams/my-stream",
                output_format="org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
                ser_de_info=aws.glue.CatalogTableStorageDescriptorSerDeInfoArgs(
                    name="my-stream",
                    parameters={
                        "serialization.format": "1",
                    },
                    serialization_library="org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe",
                ),
            ),
            table_type="EXTERNAL_TABLE")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_id: ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
        :param pulumi.Input[str] database_name: Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        :param pulumi.Input[str] description: Description of the table.
        :param pulumi.Input[str] name: Name of the SerDe.
        :param pulumi.Input[str] owner: Owner of the table.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of initialization parameters for the SerDe, in key-value form.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CatalogTablePartitionKeyArgs']]]] partition_keys: A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        :param pulumi.Input[int] retention: Retention time for this table.
        :param pulumi.Input[pulumi.InputType['CatalogTableStorageDescriptorArgs']] storage_descriptor: A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
        :param pulumi.Input[str] table_type: The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
        :param pulumi.Input[str] view_expanded_text: If the table is a view, the expanded text of the view; otherwise null.
        :param pulumi.Input[str] view_original_text: If the table is a view, the original text of the view; otherwise null.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['catalog_id'] = catalog_id
            if database_name is None:
                raise TypeError("Missing required property 'database_name'")
            __props__['database_name'] = database_name
            __props__['description'] = description
            __props__['name'] = name
            __props__['owner'] = owner
            __props__['parameters'] = parameters
            __props__['partition_keys'] = partition_keys
            __props__['retention'] = retention
            __props__['storage_descriptor'] = storage_descriptor
            __props__['table_type'] = table_type
            __props__['view_expanded_text'] = view_expanded_text
            __props__['view_original_text'] = view_original_text
            __props__['arn'] = None
        super(CatalogTable, __self__).__init__(
            'aws:glue/catalogTable:CatalogTable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            catalog_id: Optional[pulumi.Input[str]] = None,
            database_name: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CatalogTablePartitionKeyArgs']]]]] = None,
            retention: Optional[pulumi.Input[int]] = None,
            storage_descriptor: Optional[pulumi.Input[pulumi.InputType['CatalogTableStorageDescriptorArgs']]] = None,
            table_type: Optional[pulumi.Input[str]] = None,
            view_expanded_text: Optional[pulumi.Input[str]] = None,
            view_original_text: Optional[pulumi.Input[str]] = None) -> 'CatalogTable':
        """
        Get an existing CatalogTable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Glue Table.
        :param pulumi.Input[str] catalog_id: ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
        :param pulumi.Input[str] database_name: Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        :param pulumi.Input[str] description: Description of the table.
        :param pulumi.Input[str] name: Name of the SerDe.
        :param pulumi.Input[str] owner: Owner of the table.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] parameters: A map of initialization parameters for the SerDe, in key-value form.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CatalogTablePartitionKeyArgs']]]] partition_keys: A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        :param pulumi.Input[int] retention: Retention time for this table.
        :param pulumi.Input[pulumi.InputType['CatalogTableStorageDescriptorArgs']] storage_descriptor: A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
        :param pulumi.Input[str] table_type: The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
        :param pulumi.Input[str] view_expanded_text: If the table is a view, the expanded text of the view; otherwise null.
        :param pulumi.Input[str] view_original_text: If the table is a view, the original text of the view; otherwise null.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["arn"] = arn
        __props__["catalog_id"] = catalog_id
        __props__["database_name"] = database_name
        __props__["description"] = description
        __props__["name"] = name
        __props__["owner"] = owner
        __props__["parameters"] = parameters
        __props__["partition_keys"] = partition_keys
        __props__["retention"] = retention
        __props__["storage_descriptor"] = storage_descriptor
        __props__["table_type"] = table_type
        __props__["view_expanded_text"] = view_expanded_text
        __props__["view_original_text"] = view_original_text
        return CatalogTable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Glue Table.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[str]:
        """
        ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
        """
        return pulumi.get(self, "catalog_id")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the table.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the SerDe.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[str]]:
        """
        Owner of the table.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of initialization parameters for the SerDe, in key-value form.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> pulumi.Output[Optional[Sequence['outputs.CatalogTablePartitionKey']]]:
        """
        A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
        """
        return pulumi.get(self, "partition_keys")

    @property
    @pulumi.getter
    def retention(self) -> pulumi.Output[Optional[int]]:
        """
        Retention time for this table.
        """
        return pulumi.get(self, "retention")

    @property
    @pulumi.getter(name="storageDescriptor")
    def storage_descriptor(self) -> pulumi.Output[Optional['outputs.CatalogTableStorageDescriptor']]:
        """
        A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
        """
        return pulumi.get(self, "storage_descriptor")

    @property
    @pulumi.getter(name="tableType")
    def table_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
        """
        return pulumi.get(self, "table_type")

    @property
    @pulumi.getter(name="viewExpandedText")
    def view_expanded_text(self) -> pulumi.Output[Optional[str]]:
        """
        If the table is a view, the expanded text of the view; otherwise null.
        """
        return pulumi.get(self, "view_expanded_text")

    @property
    @pulumi.getter(name="viewOriginalText")
    def view_original_text(self) -> pulumi.Output[Optional[str]]:
        """
        If the table is a view, the original text of the view; otherwise null.
        """
        return pulumi.get(self, "view_original_text")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

