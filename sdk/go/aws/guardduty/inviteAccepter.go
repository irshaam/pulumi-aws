// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package guardduty

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to accept a pending GuardDuty invite on creation, ensure the detector has the correct primary account on read, and disassociate with the primary account upon removal.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/guardduty"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/providers"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := providers.Newaws(ctx, "primary", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = providers.Newaws(ctx, "member", nil)
// 		if err != nil {
// 			return err
// 		}
// 		primaryDetector, err := guardduty.NewDetector(ctx, "primaryDetector", nil, pulumi.Provider(aws.Primary))
// 		if err != nil {
// 			return err
// 		}
// 		memberDetector, err := guardduty.NewDetector(ctx, "memberDetector", nil, pulumi.Provider(aws.Member))
// 		if err != nil {
// 			return err
// 		}
// 		memberMember, err := guardduty.NewMember(ctx, "memberMember", &guardduty.MemberArgs{
// 			AccountId:  memberDetector.AccountId,
// 			DetectorId: primaryDetector.ID(),
// 			Email:      pulumi.String("required@example.com"),
// 			Invite:     pulumi.Bool(true),
// 		}, pulumi.Provider(aws.Primary))
// 		if err != nil {
// 			return err
// 		}
// 		_, err = guardduty.NewInviteAccepter(ctx, "memberInviteAccepter", &guardduty.InviteAccepterArgs{
// 			DetectorId:      memberDetector.ID(),
// 			MasterAccountId: primaryDetector.AccountId,
// 		}, pulumi.Provider(aws.Member), pulumi.DependsOn([]pulumi.Resource{
// 			memberMember,
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type InviteAccepter struct {
	pulumi.CustomResourceState

	// The detector ID of the member GuardDuty account.
	DetectorId pulumi.StringOutput `pulumi:"detectorId"`
	// AWS account ID for primary account.
	MasterAccountId pulumi.StringOutput `pulumi:"masterAccountId"`
}

// NewInviteAccepter registers a new resource with the given unique name, arguments, and options.
func NewInviteAccepter(ctx *pulumi.Context,
	name string, args *InviteAccepterArgs, opts ...pulumi.ResourceOption) (*InviteAccepter, error) {
	if args == nil || args.DetectorId == nil {
		return nil, errors.New("missing required argument 'DetectorId'")
	}
	if args == nil || args.MasterAccountId == nil {
		return nil, errors.New("missing required argument 'MasterAccountId'")
	}
	if args == nil {
		args = &InviteAccepterArgs{}
	}
	var resource InviteAccepter
	err := ctx.RegisterResource("aws:guardduty/inviteAccepter:InviteAccepter", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInviteAccepter gets an existing InviteAccepter resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInviteAccepter(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InviteAccepterState, opts ...pulumi.ResourceOption) (*InviteAccepter, error) {
	var resource InviteAccepter
	err := ctx.ReadResource("aws:guardduty/inviteAccepter:InviteAccepter", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InviteAccepter resources.
type inviteAccepterState struct {
	// The detector ID of the member GuardDuty account.
	DetectorId *string `pulumi:"detectorId"`
	// AWS account ID for primary account.
	MasterAccountId *string `pulumi:"masterAccountId"`
}

type InviteAccepterState struct {
	// The detector ID of the member GuardDuty account.
	DetectorId pulumi.StringPtrInput
	// AWS account ID for primary account.
	MasterAccountId pulumi.StringPtrInput
}

func (InviteAccepterState) ElementType() reflect.Type {
	return reflect.TypeOf((*inviteAccepterState)(nil)).Elem()
}

type inviteAccepterArgs struct {
	// The detector ID of the member GuardDuty account.
	DetectorId string `pulumi:"detectorId"`
	// AWS account ID for primary account.
	MasterAccountId string `pulumi:"masterAccountId"`
}

// The set of arguments for constructing a InviteAccepter resource.
type InviteAccepterArgs struct {
	// The detector ID of the member GuardDuty account.
	DetectorId pulumi.StringInput
	// AWS account ID for primary account.
	MasterAccountId pulumi.StringInput
}

func (InviteAccepterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*inviteAccepterArgs)(nil)).Elem()
}
