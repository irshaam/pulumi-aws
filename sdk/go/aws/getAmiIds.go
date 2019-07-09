// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package aws

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get a list of AMI IDs matching the specified criteria.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ami_ids.html.markdown.
func LookupAmiIds(ctx *pulumi.Context, args *GetAmiIdsArgs) (*GetAmiIdsResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["executableUsers"] = args.ExecutableUsers
		inputs["filters"] = args.Filters
		inputs["nameRegex"] = args.NameRegex
		inputs["owners"] = args.Owners
		inputs["sortAscending"] = args.SortAscending
	}
	outputs, err := ctx.Invoke("aws:index/getAmiIds:getAmiIds", inputs)
	if err != nil {
		return nil, err
	}
	return &GetAmiIdsResult{
		ExecutableUsers: outputs["executableUsers"],
		Filters: outputs["filters"],
		Ids: outputs["ids"],
		NameRegex: outputs["nameRegex"],
		Owners: outputs["owners"],
		SortAscending: outputs["sortAscending"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getAmiIds.
type GetAmiIdsArgs struct {
	// Limit search to users with *explicit* launch
	// permission on  the image. Valid items are the numeric account ID or `self`.
	ExecutableUsers interface{}
	// One or more name/value pairs to filter off of. There
	// are several valid keys, for a full reference, check out
	// [describe-images in the AWS CLI reference][1].
	Filters interface{}
	// A regex string to apply to the AMI list returned
	// by AWS. This allows more advanced filtering not supported from the AWS API.
	// This filtering is done locally on what AWS returns, and could have a performance
	// impact if the result is large. It is recommended to combine this with other
	// options to narrow down the list AWS returns.
	NameRegex interface{}
	// List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
	Owners interface{}
	// Used to sort AMIs by creation time.
	SortAscending interface{}
}

// A collection of values returned by getAmiIds.
type GetAmiIdsResult struct {
	ExecutableUsers interface{}
	Filters interface{}
	Ids interface{}
	NameRegex interface{}
	Owners interface{}
	SortAscending interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
