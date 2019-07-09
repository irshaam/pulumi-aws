// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a Glue Crawler. More information can be found in the [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_crawler.html.markdown.
type Crawler struct {
	s *pulumi.ResourceState
}

// NewCrawler registers a new resource with the given unique name, arguments, and options.
func NewCrawler(ctx *pulumi.Context,
	name string, args *CrawlerArgs, opts ...pulumi.ResourceOpt) (*Crawler, error) {
	if args == nil || args.DatabaseName == nil {
		return nil, errors.New("missing required argument 'DatabaseName'")
	}
	if args == nil || args.Role == nil {
		return nil, errors.New("missing required argument 'Role'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["classifiers"] = nil
		inputs["configuration"] = nil
		inputs["databaseName"] = nil
		inputs["description"] = nil
		inputs["dynamodbTargets"] = nil
		inputs["jdbcTargets"] = nil
		inputs["name"] = nil
		inputs["role"] = nil
		inputs["s3Targets"] = nil
		inputs["schedule"] = nil
		inputs["schemaChangePolicy"] = nil
		inputs["securityConfiguration"] = nil
		inputs["tablePrefix"] = nil
	} else {
		inputs["classifiers"] = args.Classifiers
		inputs["configuration"] = args.Configuration
		inputs["databaseName"] = args.DatabaseName
		inputs["description"] = args.Description
		inputs["dynamodbTargets"] = args.DynamodbTargets
		inputs["jdbcTargets"] = args.JdbcTargets
		inputs["name"] = args.Name
		inputs["role"] = args.Role
		inputs["s3Targets"] = args.S3Targets
		inputs["schedule"] = args.Schedule
		inputs["schemaChangePolicy"] = args.SchemaChangePolicy
		inputs["securityConfiguration"] = args.SecurityConfiguration
		inputs["tablePrefix"] = args.TablePrefix
	}
	inputs["arn"] = nil
	s, err := ctx.RegisterResource("aws:glue/crawler:Crawler", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Crawler{s: s}, nil
}

// GetCrawler gets an existing Crawler resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCrawler(ctx *pulumi.Context,
	name string, id pulumi.ID, state *CrawlerState, opts ...pulumi.ResourceOpt) (*Crawler, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["arn"] = state.Arn
		inputs["classifiers"] = state.Classifiers
		inputs["configuration"] = state.Configuration
		inputs["databaseName"] = state.DatabaseName
		inputs["description"] = state.Description
		inputs["dynamodbTargets"] = state.DynamodbTargets
		inputs["jdbcTargets"] = state.JdbcTargets
		inputs["name"] = state.Name
		inputs["role"] = state.Role
		inputs["s3Targets"] = state.S3Targets
		inputs["schedule"] = state.Schedule
		inputs["schemaChangePolicy"] = state.SchemaChangePolicy
		inputs["securityConfiguration"] = state.SecurityConfiguration
		inputs["tablePrefix"] = state.TablePrefix
	}
	s, err := ctx.ReadResource("aws:glue/crawler:Crawler", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Crawler{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Crawler) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Crawler) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ARN of the crawler 
func (r *Crawler) Arn() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["arn"])
}

// List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
func (r *Crawler) Classifiers() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["classifiers"])
}

// JSON string of configuration information.
func (r *Crawler) Configuration() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["configuration"])
}

// Glue database where results are written.
func (r *Crawler) DatabaseName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["databaseName"])
}

// Description of the crawler.
func (r *Crawler) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// List of nested DynamoDB target arguments. See below.
func (r *Crawler) DynamodbTargets() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["dynamodbTargets"])
}

// List of nested JBDC target arguments. See below.
func (r *Crawler) JdbcTargets() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["jdbcTargets"])
}

// Name of the crawler.
func (r *Crawler) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.
func (r *Crawler) Role() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["role"])
}

// List nested Amazon S3 target arguments. See below.
func (r *Crawler) S3Targets() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["s3Targets"])
}

// A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
func (r *Crawler) Schedule() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["schedule"])
}

// Policy for the crawler's update and deletion behavior.
func (r *Crawler) SchemaChangePolicy() *pulumi.Output {
	return r.s.State["schemaChangePolicy"]
}

// The name of Security Configuration to be used by the crawler
func (r *Crawler) SecurityConfiguration() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["securityConfiguration"])
}

// The table prefix used for catalog tables that are created.
func (r *Crawler) TablePrefix() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tablePrefix"])
}

// Input properties used for looking up and filtering Crawler resources.
type CrawlerState struct {
	// The ARN of the crawler 
	Arn interface{}
	// List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
	Classifiers interface{}
	// JSON string of configuration information.
	Configuration interface{}
	// Glue database where results are written.
	DatabaseName interface{}
	// Description of the crawler.
	Description interface{}
	// List of nested DynamoDB target arguments. See below.
	DynamodbTargets interface{}
	// List of nested JBDC target arguments. See below.
	JdbcTargets interface{}
	// Name of the crawler.
	Name interface{}
	// The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.
	Role interface{}
	// List nested Amazon S3 target arguments. See below.
	S3Targets interface{}
	// A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
	Schedule interface{}
	// Policy for the crawler's update and deletion behavior.
	SchemaChangePolicy interface{}
	// The name of Security Configuration to be used by the crawler
	SecurityConfiguration interface{}
	// The table prefix used for catalog tables that are created.
	TablePrefix interface{}
}

// The set of arguments for constructing a Crawler resource.
type CrawlerArgs struct {
	// List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.
	Classifiers interface{}
	// JSON string of configuration information.
	Configuration interface{}
	// Glue database where results are written.
	DatabaseName interface{}
	// Description of the crawler.
	Description interface{}
	// List of nested DynamoDB target arguments. See below.
	DynamodbTargets interface{}
	// List of nested JBDC target arguments. See below.
	JdbcTargets interface{}
	// Name of the crawler.
	Name interface{}
	// The IAM role friendly name (including path without leading slash), or ARN of an IAM role, used by the crawler to access other resources.
	Role interface{}
	// List nested Amazon S3 target arguments. See below.
	S3Targets interface{}
	// A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.
	Schedule interface{}
	// Policy for the crawler's update and deletion behavior.
	SchemaChangePolicy interface{}
	// The name of Security Configuration to be used by the crawler
	SecurityConfiguration interface{}
	// The table prefix used for catalog tables that are created.
	TablePrefix interface{}
}
