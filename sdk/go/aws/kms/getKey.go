// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get detailed information about 
// the specified KMS Key with flexible key id input. 
// This can be useful to reference key alias 
// without having to hard code the ARN as input.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/kms_key.html.markdown.
func LookupKey(ctx *pulumi.Context, args *GetKeyArgs) (*GetKeyResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["grantTokens"] = args.GrantTokens
		inputs["keyId"] = args.KeyId
	}
	outputs, err := ctx.Invoke("aws:kms/getKey:getKey", inputs)
	if err != nil {
		return nil, err
	}
	return &GetKeyResult{
		Arn: outputs["arn"],
		AwsAccountId: outputs["awsAccountId"],
		CreationDate: outputs["creationDate"],
		DeletionDate: outputs["deletionDate"],
		Description: outputs["description"],
		Enabled: outputs["enabled"],
		ExpirationModel: outputs["expirationModel"],
		GrantTokens: outputs["grantTokens"],
		KeyId: outputs["keyId"],
		KeyManager: outputs["keyManager"],
		KeyState: outputs["keyState"],
		KeyUsage: outputs["keyUsage"],
		Origin: outputs["origin"],
		ValidTo: outputs["validTo"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getKey.
type GetKeyArgs struct {
	// List of grant tokens
	GrantTokens interface{}
	// Key identifier which can be one of the following format:
	// * Key ID. E.g: `1234abcd-12ab-34cd-56ef-1234567890ab`
	// * Key ARN. E.g.: `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
	// * Alias name. E.g.: `alias/my-key`
	// * Alias ARN: E.g.: `arn:aws:kms:us-east-1:111122223333:alias/my-key`
	KeyId interface{}
}

// A collection of values returned by getKey.
type GetKeyResult struct {
	Arn interface{}
	AwsAccountId interface{}
	CreationDate interface{}
	DeletionDate interface{}
	Description interface{}
	Enabled interface{}
	ExpirationModel interface{}
	GrantTokens interface{}
	KeyId interface{}
	KeyManager interface{}
	KeyState interface{}
	KeyUsage interface{}
	Origin interface{}
	ValidTo interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
