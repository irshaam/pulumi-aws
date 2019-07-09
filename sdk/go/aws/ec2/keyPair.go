// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an [EC2 key pair](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html) resource. A key pair is used to control login access to EC2 instances.
// 
// Currently this resource requires an existing user-supplied key pair. This key pair's public key will be registered with AWS to allow logging-in to EC2 instances.
// 
// When importing an existing key pair the public key material may be in any format supported by AWS. Supported formats (per the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws)) are:
// 
// * OpenSSH public key format (the format in ~/.ssh/authorized_keys)
// * Base64 encoded DER format
// * SSH public key file format as specified in RFC4716
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/key_pair.html.markdown.
type KeyPair struct {
	s *pulumi.ResourceState
}

// NewKeyPair registers a new resource with the given unique name, arguments, and options.
func NewKeyPair(ctx *pulumi.Context,
	name string, args *KeyPairArgs, opts ...pulumi.ResourceOpt) (*KeyPair, error) {
	if args == nil || args.PublicKey == nil {
		return nil, errors.New("missing required argument 'PublicKey'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["keyName"] = nil
		inputs["keyNamePrefix"] = nil
		inputs["publicKey"] = nil
	} else {
		inputs["keyName"] = args.KeyName
		inputs["keyNamePrefix"] = args.KeyNamePrefix
		inputs["publicKey"] = args.PublicKey
	}
	inputs["fingerprint"] = nil
	s, err := ctx.RegisterResource("aws:ec2/keyPair:KeyPair", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &KeyPair{s: s}, nil
}

// GetKeyPair gets an existing KeyPair resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKeyPair(ctx *pulumi.Context,
	name string, id pulumi.ID, state *KeyPairState, opts ...pulumi.ResourceOpt) (*KeyPair, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["fingerprint"] = state.Fingerprint
		inputs["keyName"] = state.KeyName
		inputs["keyNamePrefix"] = state.KeyNamePrefix
		inputs["publicKey"] = state.PublicKey
	}
	s, err := ctx.ReadResource("aws:ec2/keyPair:KeyPair", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &KeyPair{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *KeyPair) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *KeyPair) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The MD5 public key fingerprint as specified in section 4 of RFC 4716.
func (r *KeyPair) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

// The name for the key pair.
func (r *KeyPair) KeyName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["keyName"])
}

// Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.
func (r *KeyPair) KeyNamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["keyNamePrefix"])
}

// The public key material.
func (r *KeyPair) PublicKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicKey"])
}

// Input properties used for looking up and filtering KeyPair resources.
type KeyPairState struct {
	// The MD5 public key fingerprint as specified in section 4 of RFC 4716.
	Fingerprint interface{}
	// The name for the key pair.
	KeyName interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.
	KeyNamePrefix interface{}
	// The public key material.
	PublicKey interface{}
}

// The set of arguments for constructing a KeyPair resource.
type KeyPairArgs struct {
	// The name for the key pair.
	KeyName interface{}
	// Creates a unique name beginning with the specified prefix. Conflicts with `key_name`.
	KeyNamePrefix interface{}
	// The public key material.
	PublicKey interface{}
}
