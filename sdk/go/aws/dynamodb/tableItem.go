// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dynamodb

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a DynamoDB table item resource
// 
// > **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
//   You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table_item.html.markdown.
type TableItem struct {
	s *pulumi.ResourceState
}

// NewTableItem registers a new resource with the given unique name, arguments, and options.
func NewTableItem(ctx *pulumi.Context,
	name string, args *TableItemArgs, opts ...pulumi.ResourceOpt) (*TableItem, error) {
	if args == nil || args.HashKey == nil {
		return nil, errors.New("missing required argument 'HashKey'")
	}
	if args == nil || args.Item == nil {
		return nil, errors.New("missing required argument 'Item'")
	}
	if args == nil || args.TableName == nil {
		return nil, errors.New("missing required argument 'TableName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["hashKey"] = nil
		inputs["item"] = nil
		inputs["rangeKey"] = nil
		inputs["tableName"] = nil
	} else {
		inputs["hashKey"] = args.HashKey
		inputs["item"] = args.Item
		inputs["rangeKey"] = args.RangeKey
		inputs["tableName"] = args.TableName
	}
	s, err := ctx.RegisterResource("aws:dynamodb/tableItem:TableItem", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TableItem{s: s}, nil
}

// GetTableItem gets an existing TableItem resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTableItem(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TableItemState, opts ...pulumi.ResourceOpt) (*TableItem, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["hashKey"] = state.HashKey
		inputs["item"] = state.Item
		inputs["rangeKey"] = state.RangeKey
		inputs["tableName"] = state.TableName
	}
	s, err := ctx.ReadResource("aws:dynamodb/tableItem:TableItem", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &TableItem{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *TableItem) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *TableItem) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Hash key to use for lookups and identification of the item
func (r *TableItem) HashKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["hashKey"])
}

// JSON representation of a map of attribute name/value pairs, one for each attribute.
// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
func (r *TableItem) Item() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["item"])
}

// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
func (r *TableItem) RangeKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["rangeKey"])
}

// The name of the table to contain the item.
func (r *TableItem) TableName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tableName"])
}

// Input properties used for looking up and filtering TableItem resources.
type TableItemState struct {
	// Hash key to use for lookups and identification of the item
	HashKey interface{}
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item interface{}
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey interface{}
	// The name of the table to contain the item.
	TableName interface{}
}

// The set of arguments for constructing a TableItem resource.
type TableItemArgs struct {
	// Hash key to use for lookups and identification of the item
	HashKey interface{}
	// JSON representation of a map of attribute name/value pairs, one for each attribute.
	// Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.
	Item interface{}
	// Range key to use for lookups and identification of the item. Required if there is range key defined in the table.
	RangeKey interface{}
	// The name of the table to contain the item.
	TableName interface{}
}
