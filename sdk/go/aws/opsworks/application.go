// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package opsworks

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides an OpsWorks application resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_application.html.markdown.
type Application struct {
	s *pulumi.ResourceState
}

// NewApplication registers a new resource with the given unique name, arguments, and options.
func NewApplication(ctx *pulumi.Context,
	name string, args *ApplicationArgs, opts ...pulumi.ResourceOpt) (*Application, error) {
	if args == nil || args.StackId == nil {
		return nil, errors.New("missing required argument 'StackId'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["appSources"] = nil
		inputs["autoBundleOnDeploy"] = nil
		inputs["awsFlowRubySettings"] = nil
		inputs["dataSourceArn"] = nil
		inputs["dataSourceDatabaseName"] = nil
		inputs["dataSourceType"] = nil
		inputs["description"] = nil
		inputs["documentRoot"] = nil
		inputs["domains"] = nil
		inputs["enableSsl"] = nil
		inputs["environments"] = nil
		inputs["name"] = nil
		inputs["railsEnv"] = nil
		inputs["shortName"] = nil
		inputs["sslConfigurations"] = nil
		inputs["stackId"] = nil
		inputs["type"] = nil
	} else {
		inputs["appSources"] = args.AppSources
		inputs["autoBundleOnDeploy"] = args.AutoBundleOnDeploy
		inputs["awsFlowRubySettings"] = args.AwsFlowRubySettings
		inputs["dataSourceArn"] = args.DataSourceArn
		inputs["dataSourceDatabaseName"] = args.DataSourceDatabaseName
		inputs["dataSourceType"] = args.DataSourceType
		inputs["description"] = args.Description
		inputs["documentRoot"] = args.DocumentRoot
		inputs["domains"] = args.Domains
		inputs["enableSsl"] = args.EnableSsl
		inputs["environments"] = args.Environments
		inputs["name"] = args.Name
		inputs["railsEnv"] = args.RailsEnv
		inputs["shortName"] = args.ShortName
		inputs["sslConfigurations"] = args.SslConfigurations
		inputs["stackId"] = args.StackId
		inputs["type"] = args.Type
	}
	s, err := ctx.RegisterResource("aws:opsworks/application:Application", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Application{s: s}, nil
}

// GetApplication gets an existing Application resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplication(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ApplicationState, opts ...pulumi.ResourceOpt) (*Application, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["appSources"] = state.AppSources
		inputs["autoBundleOnDeploy"] = state.AutoBundleOnDeploy
		inputs["awsFlowRubySettings"] = state.AwsFlowRubySettings
		inputs["dataSourceArn"] = state.DataSourceArn
		inputs["dataSourceDatabaseName"] = state.DataSourceDatabaseName
		inputs["dataSourceType"] = state.DataSourceType
		inputs["description"] = state.Description
		inputs["documentRoot"] = state.DocumentRoot
		inputs["domains"] = state.Domains
		inputs["enableSsl"] = state.EnableSsl
		inputs["environments"] = state.Environments
		inputs["name"] = state.Name
		inputs["railsEnv"] = state.RailsEnv
		inputs["shortName"] = state.ShortName
		inputs["sslConfigurations"] = state.SslConfigurations
		inputs["stackId"] = state.StackId
		inputs["type"] = state.Type
	}
	s, err := ctx.ReadResource("aws:opsworks/application:Application", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Application{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Application) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Application) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// SCM configuration of the app as described below.
func (r *Application) AppSources() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["appSources"])
}

// Run bundle install when deploying for application of type `rails`.
func (r *Application) AutoBundleOnDeploy() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["autoBundleOnDeploy"])
}

// Specify activity and workflow workers for your app using the aws-flow gem.
func (r *Application) AwsFlowRubySettings() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["awsFlowRubySettings"])
}

// The data source's ARN.
func (r *Application) DataSourceArn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dataSourceArn"])
}

// The database name.
func (r *Application) DataSourceDatabaseName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dataSourceDatabaseName"])
}

// The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.
func (r *Application) DataSourceType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dataSourceType"])
}

// A description of the app.
func (r *Application) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// Subfolder for the document root for application of type `rails`.
func (r *Application) DocumentRoot() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["documentRoot"])
}

// A list of virtual host alias.
func (r *Application) Domains() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["domains"])
}

// Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.
func (r *Application) EnableSsl() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enableSsl"])
}

// Object to define environment variables.  Object is described below.
func (r *Application) Environments() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["environments"])
}

// A human-readable name for the application.
func (r *Application) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The name of the Rails environment for application of type `rails`.
func (r *Application) RailsEnv() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["railsEnv"])
}

// A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.
func (r *Application) ShortName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["shortName"])
}

// The SSL configuration of the app. Object is described below.
func (r *Application) SslConfigurations() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["sslConfigurations"])
}

// The id of the stack the application will belong to.
func (r *Application) StackId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["stackId"])
}

// The type of source to use. For example, "archive".
func (r *Application) Type() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["type"])
}

// Input properties used for looking up and filtering Application resources.
type ApplicationState struct {
	// SCM configuration of the app as described below.
	AppSources interface{}
	// Run bundle install when deploying for application of type `rails`.
	AutoBundleOnDeploy interface{}
	// Specify activity and workflow workers for your app using the aws-flow gem.
	AwsFlowRubySettings interface{}
	// The data source's ARN.
	DataSourceArn interface{}
	// The database name.
	DataSourceDatabaseName interface{}
	// The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.
	DataSourceType interface{}
	// A description of the app.
	Description interface{}
	// Subfolder for the document root for application of type `rails`.
	DocumentRoot interface{}
	// A list of virtual host alias.
	Domains interface{}
	// Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.
	EnableSsl interface{}
	// Object to define environment variables.  Object is described below.
	Environments interface{}
	// A human-readable name for the application.
	Name interface{}
	// The name of the Rails environment for application of type `rails`.
	RailsEnv interface{}
	// A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.
	ShortName interface{}
	// The SSL configuration of the app. Object is described below.
	SslConfigurations interface{}
	// The id of the stack the application will belong to.
	StackId interface{}
	// The type of source to use. For example, "archive".
	Type interface{}
}

// The set of arguments for constructing a Application resource.
type ApplicationArgs struct {
	// SCM configuration of the app as described below.
	AppSources interface{}
	// Run bundle install when deploying for application of type `rails`.
	AutoBundleOnDeploy interface{}
	// Specify activity and workflow workers for your app using the aws-flow gem.
	AwsFlowRubySettings interface{}
	// The data source's ARN.
	DataSourceArn interface{}
	// The database name.
	DataSourceDatabaseName interface{}
	// The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.
	DataSourceType interface{}
	// A description of the app.
	Description interface{}
	// Subfolder for the document root for application of type `rails`.
	DocumentRoot interface{}
	// A list of virtual host alias.
	Domains interface{}
	// Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.
	EnableSsl interface{}
	// Object to define environment variables.  Object is described below.
	Environments interface{}
	// A human-readable name for the application.
	Name interface{}
	// The name of the Rails environment for application of type `rails`.
	RailsEnv interface{}
	// A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.
	ShortName interface{}
	// The SSL configuration of the app. Object is described below.
	SslConfigurations interface{}
	// The id of the stack the application will belong to.
	StackId interface{}
	// The type of source to use. For example, "archive".
	Type interface{}
}
