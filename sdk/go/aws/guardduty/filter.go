// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage a GuardDuty filter.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/guardduty"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := guardduty.NewFilter(ctx, "myFilter", &guardduty.FilterArgs{
// 			Action:     pulumi.String("ARCHIVE"),
// 			DetectorId: pulumi.Any(aws_guardduty_detector.Example.Id),
// 			Rank:       pulumi.Int(1),
// 			FindingCriteria: &guardduty.FilterFindingCriteriaArgs{
// 				Criterions: guardduty.FilterFindingCriteriaCriterionArray{
// 					&guardduty.FilterFindingCriteriaCriterionArgs{
// 						Field: pulumi.String("region"),
// 						Equals: pulumi.StringArray{
// 							pulumi.String("eu-west-1"),
// 						},
// 					},
// 					&guardduty.FilterFindingCriteriaCriterionArgs{
// 						Field: pulumi.String("service.additionalInfo.threatListName"),
// 						NotEquals: pulumi.StringArray{
// 							pulumi.String("some-threat"),
// 							pulumi.String("another-threat"),
// 						},
// 					},
// 					&guardduty.FilterFindingCriteriaCriterionArgs{
// 						Field:       pulumi.String("updatedAt"),
// 						GreaterThan: pulumi.String("2020-01-01T00:00:00Z"),
// 						LessThan:    pulumi.String("2020-02-01T00:00:00Z"),
// 					},
// 					&guardduty.FilterFindingCriteriaCriterionArgs{
// 						Field:              pulumi.String("severity"),
// 						GreaterThanOrEqual: pulumi.String("4"),
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Filter struct {
	pulumi.CustomResourceState

	// Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
	Action pulumi.StringOutput `pulumi:"action"`
	// The ARN of the GuardDuty filter.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Description of the filter.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// ID of a GuardDuty detector, attached to your account.
	DetectorId pulumi.StringOutput `pulumi:"detectorId"`
	// Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
	FindingCriteria FilterFindingCriteriaOutput `pulumi:"findingCriteria"`
	// The name of your filter.
	Name pulumi.StringOutput `pulumi:"name"`
	// Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
	Rank pulumi.IntOutput `pulumi:"rank"`
	// The tags that you want to add to the Filter resource. A tag consists of a key and a value.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewFilter registers a new resource with the given unique name, arguments, and options.
func NewFilter(ctx *pulumi.Context,
	name string, args *FilterArgs, opts ...pulumi.ResourceOption) (*Filter, error) {
	if args == nil || args.Action == nil {
		return nil, errors.New("missing required argument 'Action'")
	}
	if args == nil || args.DetectorId == nil {
		return nil, errors.New("missing required argument 'DetectorId'")
	}
	if args == nil || args.FindingCriteria == nil {
		return nil, errors.New("missing required argument 'FindingCriteria'")
	}
	if args == nil || args.Rank == nil {
		return nil, errors.New("missing required argument 'Rank'")
	}
	if args == nil {
		args = &FilterArgs{}
	}
	var resource Filter
	err := ctx.RegisterResource("aws:guardduty/filter:Filter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFilter gets an existing Filter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFilter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FilterState, opts ...pulumi.ResourceOption) (*Filter, error) {
	var resource Filter
	err := ctx.ReadResource("aws:guardduty/filter:Filter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Filter resources.
type filterState struct {
	// Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
	Action *string `pulumi:"action"`
	// The ARN of the GuardDuty filter.
	Arn *string `pulumi:"arn"`
	// Description of the filter.
	Description *string `pulumi:"description"`
	// ID of a GuardDuty detector, attached to your account.
	DetectorId *string `pulumi:"detectorId"`
	// Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
	FindingCriteria *FilterFindingCriteria `pulumi:"findingCriteria"`
	// The name of your filter.
	Name *string `pulumi:"name"`
	// Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
	Rank *int `pulumi:"rank"`
	// The tags that you want to add to the Filter resource. A tag consists of a key and a value.
	Tags map[string]string `pulumi:"tags"`
}

type FilterState struct {
	// Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
	Action pulumi.StringPtrInput
	// The ARN of the GuardDuty filter.
	Arn pulumi.StringPtrInput
	// Description of the filter.
	Description pulumi.StringPtrInput
	// ID of a GuardDuty detector, attached to your account.
	DetectorId pulumi.StringPtrInput
	// Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
	FindingCriteria FilterFindingCriteriaPtrInput
	// The name of your filter.
	Name pulumi.StringPtrInput
	// Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
	Rank pulumi.IntPtrInput
	// The tags that you want to add to the Filter resource. A tag consists of a key and a value.
	Tags pulumi.StringMapInput
}

func (FilterState) ElementType() reflect.Type {
	return reflect.TypeOf((*filterState)(nil)).Elem()
}

type filterArgs struct {
	// Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
	Action string `pulumi:"action"`
	// Description of the filter.
	Description *string `pulumi:"description"`
	// ID of a GuardDuty detector, attached to your account.
	DetectorId string `pulumi:"detectorId"`
	// Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
	FindingCriteria FilterFindingCriteria `pulumi:"findingCriteria"`
	// The name of your filter.
	Name *string `pulumi:"name"`
	// Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
	Rank int `pulumi:"rank"`
	// The tags that you want to add to the Filter resource. A tag consists of a key and a value.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a Filter resource.
type FilterArgs struct {
	// Specifies the action that is to be applied to the findings that match the filter. Can be one of `ARCHIVE` or `NOOP`.
	Action pulumi.StringInput
	// Description of the filter.
	Description pulumi.StringPtrInput
	// ID of a GuardDuty detector, attached to your account.
	DetectorId pulumi.StringInput
	// Represents the criteria to be used in the filter for querying findings. Contains one or more `criterion` blocks, documented below.
	FindingCriteria FilterFindingCriteriaInput
	// The name of your filter.
	Name pulumi.StringPtrInput
	// Specifies the position of the filter in the list of current filters. Also specifies the order in which this filter is applied to the findings.
	Rank pulumi.IntInput
	// The tags that you want to add to the Filter resource. A tag consists of a key and a value.
	Tags pulumi.StringMapInput
}

func (FilterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*filterArgs)(nil)).Elem()
}
