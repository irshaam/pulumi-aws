// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package iam

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an IAM Server Certificate resource to upload Server Certificates.
// Certs uploaded to IAM can easily work with other AWS services such as:
// 
// - AWS Elastic Beanstalk
// - Elastic Load Balancing
// - CloudFront
// - AWS OpsWorks
// 
// For information about server certificates in IAM, see [Managing Server
// Certificates][2] in AWS Documentation.
// 
// > **Note:** All arguments including the private key will be stored in the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/iam_server_certificate.html.markdown.
type ServerCertificate struct {
	s *pulumi.ResourceState
}

// NewServerCertificate registers a new resource with the given unique name, arguments, and options.
func NewServerCertificate(ctx *pulumi.Context,
	name string, args *ServerCertificateArgs, opts ...pulumi.ResourceOpt) (*ServerCertificate, error) {
	if args == nil || args.CertificateBody == nil {
		return nil, errors.New("missing required argument 'CertificateBody'")
	}
	if args == nil || args.PrivateKey == nil {
		return nil, errors.New("missing required argument 'PrivateKey'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["arn"] = nil
		inputs["certificateBody"] = nil
		inputs["certificateChain"] = nil
		inputs["name"] = nil
		inputs["namePrefix"] = nil
		inputs["path"] = nil
		inputs["privateKey"] = nil
	} else {
		inputs["arn"] = args.Arn
		inputs["certificateBody"] = args.CertificateBody
		inputs["certificateChain"] = args.CertificateChain
		inputs["name"] = args.Name
		inputs["namePrefix"] = args.NamePrefix
		inputs["path"] = args.Path
		inputs["privateKey"] = args.PrivateKey
	}
	s, err := ctx.RegisterResource("aws:iam/serverCertificate:ServerCertificate", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ServerCertificate{s: s}, nil
}

// GetServerCertificate gets an existing ServerCertificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServerCertificate(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ServerCertificateState, opts ...pulumi.ResourceOpt) (*ServerCertificate, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["certificateBody"] = state.CertificateBody
		inputs["certificateChain"] = state.CertificateChain
		inputs["name"] = state.Name
		inputs["namePrefix"] = state.NamePrefix
		inputs["path"] = state.Path
		inputs["privateKey"] = state.PrivateKey
	}
	s, err := ctx.ReadResource("aws:iam/serverCertificate:ServerCertificate", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ServerCertificate{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ServerCertificate) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ServerCertificate) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The Amazon Resource Name (ARN) specifying the server certificate.
func (r *ServerCertificate) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// The contents of the public key certificate in
// PEM-encoded format.
func (r *ServerCertificate) CertificateBody() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateBody"])
}

// The contents of the certificate chain.
// This is typically a concatenation of the PEM-encoded public key certificates
// of the chain.
func (r *ServerCertificate) CertificateChain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificateChain"])
}

// The name of the Server Certificate
func (r *ServerCertificate) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Creates a unique name beginning with the specified
// prefix. Conflicts with `name`.
func (r *ServerCertificate) NamePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["namePrefix"])
}

// The IAM path for the server certificate.  If it is not
// included, it defaults to a slash (/). If this certificate is for use with
// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
// See [IAM Identifiers][1] for more details on IAM Paths.
func (r *ServerCertificate) Path() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["path"])
}

// The contents of the private key in PEM-encoded format.
func (r *ServerCertificate) PrivateKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateKey"])
}

// Input properties used for looking up and filtering ServerCertificate resources.
type ServerCertificateState struct {
	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn interface{}
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody interface{}
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain interface{}
	// The name of the Server Certificate
	Name interface{}
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers][1] for more details on IAM Paths.
	Path interface{}
	// The contents of the private key in PEM-encoded format.
	PrivateKey interface{}
}

// The set of arguments for constructing a ServerCertificate resource.
type ServerCertificateArgs struct {
	// The Amazon Resource Name (ARN) specifying the server certificate.
	Arn interface{}
	// The contents of the public key certificate in
	// PEM-encoded format.
	CertificateBody interface{}
	// The contents of the certificate chain.
	// This is typically a concatenation of the PEM-encoded public key certificates
	// of the chain.
	CertificateChain interface{}
	// The name of the Server Certificate
	Name interface{}
	// Creates a unique name beginning with the specified
	// prefix. Conflicts with `name`.
	NamePrefix interface{}
	// The IAM path for the server certificate.  If it is not
	// included, it defaults to a slash (/). If this certificate is for use with
	// AWS CloudFront, the path must be in format `/cloudfront/your_path_here`.
	// See [IAM Identifiers][1] for more details on IAM Paths.
	Path interface{}
	// The contents of the private key in PEM-encoded format.
	PrivateKey interface{}
}
