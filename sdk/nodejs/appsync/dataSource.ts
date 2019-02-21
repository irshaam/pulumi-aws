// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides an AppSync DataSource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const exampleGraphQLApi = new aws.appsync.GraphQLApi("example", {
 *     authenticationType: "API_KEY",
 * });
 * const exampleTable = new aws.dynamodb.Table("example", {
 *     attributes: [{
 *         name: "UserId",
 *         type: "S",
 *     }],
 *     hashKey: "UserId",
 *     readCapacity: 1,
 *     writeCapacity: 1,
 * });
 * const exampleRole = new aws.iam.Role("example", {
 *     assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": "sts:AssumeRole",
 *       "Principal": {
 *         "Service": "appsync.amazonaws.com"
 *       },
 *       "Effect": "Allow"
 *     }
 *   ]
 * }
 * `,
 * });
 * const exampleDataSource = new aws.appsync.DataSource("example", {
 *     apiId: exampleGraphQLApi.id,
 *     dynamodbConfig: {
 *         tableName: exampleTable.name,
 *     },
 *     serviceRoleArn: exampleRole.arn,
 *     type: "AMAZON_DYNAMODB",
 * });
 * const exampleRolePolicy = new aws.iam.RolePolicy("example", {
 *     policy: exampleTable.arn.apply(arn => `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Action": [
 *         "dynamodb:*"
 *       ],
 *       "Effect": "Allow",
 *       "Resource": [
 *         "${arn}"
 *       ]
 *     }
 *   ]
 * }
 * `),
 *     role: exampleRole.id,
 * });
 * ```
 */
export class DataSource extends pulumi.CustomResource {
    /**
     * Get an existing DataSource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DataSourceState, opts?: pulumi.CustomResourceOptions): DataSource {
        return new DataSource(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<DataSourceResult> {
        return ctx.list({...args, type: 'aws:appsync/dataSource:DataSource'});
    }

    /**
     * The API ID for the GraphQL API for the DataSource.
     */
    public readonly apiId: pulumi.Output<string>;
    /**
     * The ARN
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * A description of the DataSource.
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * DynamoDB settings. See below
     */
    public readonly dynamodbConfig: pulumi.Output<{ region: string, tableName: string, useCallerCredentials?: boolean } | undefined>;
    /**
     * Amazon Elasticsearch settings. See below
     */
    public readonly elasticsearchConfig: pulumi.Output<{ endpoint: string, region: string } | undefined>;
    /**
     * HTTP settings. See below
     */
    public readonly httpConfig: pulumi.Output<{ endpoint: string } | undefined>;
    /**
     * AWS Lambda settings. See below
     */
    public readonly lambdaConfig: pulumi.Output<{ functionArn: string } | undefined>;
    /**
     * A user-supplied name for the DataSource.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The IAM service role ARN for the data source.
     */
    public readonly serviceRoleArn: pulumi.Output<string | undefined>;
    /**
     * The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
     */
    public readonly type: pulumi.Output<string>;

    /**
     * Create a DataSource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DataSourceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DataSourceArgs | DataSourceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DataSourceState = argsOrState as DataSourceState | undefined;
            inputs["apiId"] = state ? state.apiId : undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["dynamodbConfig"] = state ? state.dynamodbConfig : undefined;
            inputs["elasticsearchConfig"] = state ? state.elasticsearchConfig : undefined;
            inputs["httpConfig"] = state ? state.httpConfig : undefined;
            inputs["lambdaConfig"] = state ? state.lambdaConfig : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["serviceRoleArn"] = state ? state.serviceRoleArn : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as DataSourceArgs | undefined;
            if (!args || args.apiId === undefined) {
                throw new Error("Missing required property 'apiId'");
            }
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["apiId"] = args ? args.apiId : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["dynamodbConfig"] = args ? args.dynamodbConfig : undefined;
            inputs["elasticsearchConfig"] = args ? args.elasticsearchConfig : undefined;
            inputs["httpConfig"] = args ? args.httpConfig : undefined;
            inputs["lambdaConfig"] = args ? args.lambdaConfig : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["serviceRoleArn"] = args ? args.serviceRoleArn : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:appsync/dataSource:DataSource", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DataSource resources.
 */
export interface DataSourceState {
    /**
     * The API ID for the GraphQL API for the DataSource.
     */
    readonly apiId?: pulumi.Input<string>;
    /**
     * The ARN
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * A description of the DataSource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * DynamoDB settings. See below
     */
    readonly dynamodbConfig?: pulumi.Input<{ region?: pulumi.Input<string>, tableName: pulumi.Input<string>, useCallerCredentials?: pulumi.Input<boolean> }>;
    /**
     * Amazon Elasticsearch settings. See below
     */
    readonly elasticsearchConfig?: pulumi.Input<{ endpoint: pulumi.Input<string>, region?: pulumi.Input<string> }>;
    /**
     * HTTP settings. See below
     */
    readonly httpConfig?: pulumi.Input<{ endpoint: pulumi.Input<string> }>;
    /**
     * AWS Lambda settings. See below
     */
    readonly lambdaConfig?: pulumi.Input<{ functionArn: pulumi.Input<string> }>;
    /**
     * A user-supplied name for the DataSource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The IAM service role ARN for the data source.
     */
    readonly serviceRoleArn?: pulumi.Input<string>;
    /**
     * The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
     */
    readonly type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DataSource resource.
 */
export interface DataSourceArgs {
    /**
     * The API ID for the GraphQL API for the DataSource.
     */
    readonly apiId: pulumi.Input<string>;
    /**
     * A description of the DataSource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * DynamoDB settings. See below
     */
    readonly dynamodbConfig?: pulumi.Input<{ region?: pulumi.Input<string>, tableName: pulumi.Input<string>, useCallerCredentials?: pulumi.Input<boolean> }>;
    /**
     * Amazon Elasticsearch settings. See below
     */
    readonly elasticsearchConfig?: pulumi.Input<{ endpoint: pulumi.Input<string>, region?: pulumi.Input<string> }>;
    /**
     * HTTP settings. See below
     */
    readonly httpConfig?: pulumi.Input<{ endpoint: pulumi.Input<string> }>;
    /**
     * AWS Lambda settings. See below
     */
    readonly lambdaConfig?: pulumi.Input<{ functionArn: pulumi.Input<string> }>;
    /**
     * A user-supplied name for the DataSource.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The IAM service role ARN for the data source.
     */
    readonly serviceRoleArn?: pulumi.Input<string>;
    /**
     * The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
     */
    readonly type: pulumi.Input<string>;
}

/**
 * The live DataSource resource.
 */
export interface DataSourceResult {
    /**
     * The API ID for the GraphQL API for the DataSource.
     */
    readonly apiId: string;
    /**
     * The ARN
     */
    readonly arn: string;
    /**
     * A description of the DataSource.
     */
    readonly description?: string;
    /**
     * DynamoDB settings. See below
     */
    readonly dynamodbConfig?: { region: string, tableName: string, useCallerCredentials?: boolean };
    /**
     * Amazon Elasticsearch settings. See below
     */
    readonly elasticsearchConfig?: { endpoint: string, region: string };
    /**
     * HTTP settings. See below
     */
    readonly httpConfig?: { endpoint: string };
    /**
     * AWS Lambda settings. See below
     */
    readonly lambdaConfig?: { functionArn: string };
    /**
     * A user-supplied name for the DataSource.
     */
    readonly name: string;
    /**
     * The IAM service role ARN for the data source.
     */
    readonly serviceRoleArn?: string;
    /**
     * The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
     */
    readonly type: string;
}
