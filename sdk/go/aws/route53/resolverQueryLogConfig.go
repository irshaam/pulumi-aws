// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package route53

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Route 53 Resolver query logging configuration resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/route53"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := route53.NewResolverQueryLogConfig(ctx, "example", &route53.ResolverQueryLogConfigArgs{
// 			DestinationArn: pulumi.Any(aws_s3_bucket.Example.Arn),
// 			Tags: pulumi.StringMap{
// 				"Environment": pulumi.String("Prod"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type ResolverQueryLogConfig struct {
	pulumi.CustomResourceState

	// The ARN (Amazon Resource Name) of the Route 53 Resolver query logging configuration.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ARN of the resource that you want Route 53 Resolver to send query logs.
	// You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
	DestinationArn pulumi.StringOutput `pulumi:"destinationArn"`
	// The name of the Route 53 Resolver query logging configuration.
	Name pulumi.StringOutput `pulumi:"name"`
	// The AWS account ID of the account that created the query logging configuration.
	OwnerId pulumi.StringOutput `pulumi:"ownerId"`
	// An indication of whether the query logging configuration is shared with other AWS accounts, or was shared with the current account by another AWS account.
	// Sharing is configured through AWS Resource Access Manager (AWS RAM).
	// Values are `NOT_SHARED`, `SHARED_BY_ME` or `SHARED_WITH_ME`
	ShareStatus pulumi.StringOutput `pulumi:"shareStatus"`
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapOutput `pulumi:"tags"`
}

// NewResolverQueryLogConfig registers a new resource with the given unique name, arguments, and options.
func NewResolverQueryLogConfig(ctx *pulumi.Context,
	name string, args *ResolverQueryLogConfigArgs, opts ...pulumi.ResourceOption) (*ResolverQueryLogConfig, error) {
	if args == nil || args.DestinationArn == nil {
		return nil, errors.New("missing required argument 'DestinationArn'")
	}
	if args == nil {
		args = &ResolverQueryLogConfigArgs{}
	}
	var resource ResolverQueryLogConfig
	err := ctx.RegisterResource("aws:route53/resolverQueryLogConfig:ResolverQueryLogConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResolverQueryLogConfig gets an existing ResolverQueryLogConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResolverQueryLogConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResolverQueryLogConfigState, opts ...pulumi.ResourceOption) (*ResolverQueryLogConfig, error) {
	var resource ResolverQueryLogConfig
	err := ctx.ReadResource("aws:route53/resolverQueryLogConfig:ResolverQueryLogConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResolverQueryLogConfig resources.
type resolverQueryLogConfigState struct {
	// The ARN (Amazon Resource Name) of the Route 53 Resolver query logging configuration.
	Arn *string `pulumi:"arn"`
	// The ARN of the resource that you want Route 53 Resolver to send query logs.
	// You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
	DestinationArn *string `pulumi:"destinationArn"`
	// The name of the Route 53 Resolver query logging configuration.
	Name *string `pulumi:"name"`
	// The AWS account ID of the account that created the query logging configuration.
	OwnerId *string `pulumi:"ownerId"`
	// An indication of whether the query logging configuration is shared with other AWS accounts, or was shared with the current account by another AWS account.
	// Sharing is configured through AWS Resource Access Manager (AWS RAM).
	// Values are `NOT_SHARED`, `SHARED_BY_ME` or `SHARED_WITH_ME`
	ShareStatus *string `pulumi:"shareStatus"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

type ResolverQueryLogConfigState struct {
	// The ARN (Amazon Resource Name) of the Route 53 Resolver query logging configuration.
	Arn pulumi.StringPtrInput
	// The ARN of the resource that you want Route 53 Resolver to send query logs.
	// You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
	DestinationArn pulumi.StringPtrInput
	// The name of the Route 53 Resolver query logging configuration.
	Name pulumi.StringPtrInput
	// The AWS account ID of the account that created the query logging configuration.
	OwnerId pulumi.StringPtrInput
	// An indication of whether the query logging configuration is shared with other AWS accounts, or was shared with the current account by another AWS account.
	// Sharing is configured through AWS Resource Access Manager (AWS RAM).
	// Values are `NOT_SHARED`, `SHARED_BY_ME` or `SHARED_WITH_ME`
	ShareStatus pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (ResolverQueryLogConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverQueryLogConfigState)(nil)).Elem()
}

type resolverQueryLogConfigArgs struct {
	// The ARN of the resource that you want Route 53 Resolver to send query logs.
	// You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
	DestinationArn string `pulumi:"destinationArn"`
	// The name of the Route 53 Resolver query logging configuration.
	Name *string `pulumi:"name"`
	// A map of tags to assign to the resource.
	Tags map[string]string `pulumi:"tags"`
}

// The set of arguments for constructing a ResolverQueryLogConfig resource.
type ResolverQueryLogConfigArgs struct {
	// The ARN of the resource that you want Route 53 Resolver to send query logs.
	// You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
	DestinationArn pulumi.StringInput
	// The name of the Route 53 Resolver query logging configuration.
	Name pulumi.StringPtrInput
	// A map of tags to assign to the resource.
	Tags pulumi.StringMapInput
}

func (ResolverQueryLogConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resolverQueryLogConfigArgs)(nil)).Elem()
}
