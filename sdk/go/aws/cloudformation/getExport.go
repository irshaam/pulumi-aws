// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The CloudFormation Export data source allows access to stack
// exports specified in the [Output](http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html) section of the Cloudformation Template using the optional Export Property.
//
//  > Note: If you are trying to use a value from a Cloudformation Stack in the same deployment please use normal interpolation or Cloudformation Outputs.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/cloudformation"
// 	"github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ec2"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		subnetId, err := cloudformation.GetExport(ctx, &cloudformation.GetExportArgs{
// 			Name: "mySubnetIdExportName",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = ec2.NewInstance(ctx, "web", &ec2.InstanceArgs{
// 			Ami:          pulumi.String("ami-abb07bcb"),
// 			InstanceType: pulumi.String("t2.micro"),
// 			SubnetId:     pulumi.String(subnetId.Value),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetExport(ctx *pulumi.Context, args *GetExportArgs, opts ...pulumi.InvokeOption) (*GetExportResult, error) {
	var rv GetExportResult
	err := ctx.Invoke("aws:cloudformation/getExport:getExport", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getExport.
type GetExportArgs struct {
	// The name of the export as it appears in the console or from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)
	Name string `pulumi:"name"`
}

// A collection of values returned by getExport.
type GetExportResult struct {
	// The exportingStackId (AWS ARNs) equivalent `ExportingStackId` from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)
	ExportingStackId string `pulumi:"exportingStackId"`
	// The provider-assigned unique ID for this managed resource.
	Id   string `pulumi:"id"`
	Name string `pulumi:"name"`
	// The value from Cloudformation export identified by the export name found from [list-exports](http://docs.aws.amazon.com/cli/latest/reference/cloudformation/list-exports.html)
	Value string `pulumi:"value"`
}
