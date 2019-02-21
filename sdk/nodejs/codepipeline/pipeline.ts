// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides a CodePipeline.
 * 
 * > **NOTE on `aws_codepipeline`:** - the `GITHUB_TOKEN` environment variable must be set if the GitHub provider is specified.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const fooRole = new aws.iam.Role("foo", {
 *     assumeRolePolicy: `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Effect": "Allow",
 *       "Principal": {
 *         "Service": "codepipeline.amazonaws.com"
 *       },
 *       "Action": "sts:AssumeRole"
 *     }
 *   ]
 * }
 * `,
 * });
 * const fooBucket = new aws.s3.Bucket("foo", {
 *     acl: "private",
 * });
 * const s3kmskey = pulumi.output(aws.kms.getAlias({
 *     name: "alias/myKmsKey",
 * }));
 * const fooPipeline = new aws.codepipeline.Pipeline("foo", {
 *     artifactStore: {
 *         encryptionKey: {
 *             id: s3kmskey.apply(s3kmskey => s3kmskey.arn),
 *             type: "KMS",
 *         },
 *         location: fooBucket.bucket,
 *         type: "S3",
 *     },
 *     roleArn: fooRole.arn,
 *     stages: [
 *         {
 *             actions: [{
 *                 category: "Source",
 *                 configuration: {
 *                     Branch: "master",
 *                     Owner: "my-organization",
 *                     Repo: "test",
 *                 },
 *                 name: "Source",
 *                 outputArtifacts: ["test"],
 *                 owner: "ThirdParty",
 *                 provider: "GitHub",
 *                 version: "1",
 *             }],
 *             name: "Source",
 *         },
 *         {
 *             actions: [{
 *                 category: "Build",
 *                 configuration: {
 *                     ProjectName: "test",
 *                 },
 *                 inputArtifacts: ["test"],
 *                 name: "Build",
 *                 owner: "AWS",
 *                 provider: "CodeBuild",
 *                 version: "1",
 *             }],
 *             name: "Build",
 *         },
 *     ],
 * });
 * const codepipelinePolicy = new aws.iam.RolePolicy("codepipeline_policy", {
 *     policy: pulumi.all([fooBucket.arn, fooBucket.arn]).apply(([fooBucketArn, fooBucketArn1]) => `{
 *   "Version": "2012-10-17",
 *   "Statement": [
 *     {
 *       "Effect":"Allow",
 *       "Action": [
 *         "s3:GetObject",
 *         "s3:GetObjectVersion",
 *         "s3:GetBucketVersioning"
 *       ],
 *       "Resource": [
 *         "${fooBucketArn}",
 *         "${fooBucketArn1}/*"
 *       ]
 *     },
 *     {
 *       "Effect": "Allow",
 *       "Action": [
 *         "codebuild:BatchGetBuilds",
 *         "codebuild:StartBuild"
 *       ],
 *       "Resource": "*"
 *     }
 *   ]
 * }
 * `),
 *     role: aws_iam_role_codepipeline_role.id,
 * });
 * ```
 */
export class Pipeline extends pulumi.CustomResource {
    /**
     * Get an existing Pipeline resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PipelineState, opts?: pulumi.CustomResourceOptions): Pipeline {
        return new Pipeline(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<PipelineResult> {
        return ctx.list({...args, type: 'aws:codepipeline/pipeline:Pipeline'});
    }

    /**
     * The codepipeline ARN.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * An artifact_store block. Artifact stores are documented below.
     * * `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.
     */
    public readonly artifactStore: pulumi.Output<{ encryptionKey?: { id: string, type: string }, location: string, type: string }>;
    /**
     * The name of the pipeline.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.
     */
    public readonly roleArn: pulumi.Output<string>;
    public readonly stages: pulumi.Output<{ actions: { category: string, configuration?: {[key: string]: any}, inputArtifacts?: string[], name: string, outputArtifacts?: string[], owner: string, provider: string, roleArn?: string, runOrder: number, version: string }[], name: string }[]>;

    /**
     * Create a Pipeline resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: PipelineArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: PipelineArgs | PipelineState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: PipelineState = argsOrState as PipelineState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["artifactStore"] = state ? state.artifactStore : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["roleArn"] = state ? state.roleArn : undefined;
            inputs["stages"] = state ? state.stages : undefined;
        } else {
            const args = argsOrState as PipelineArgs | undefined;
            if (!args || args.artifactStore === undefined) {
                throw new Error("Missing required property 'artifactStore'");
            }
            if (!args || args.roleArn === undefined) {
                throw new Error("Missing required property 'roleArn'");
            }
            if (!args || args.stages === undefined) {
                throw new Error("Missing required property 'stages'");
            }
            inputs["artifactStore"] = args ? args.artifactStore : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["roleArn"] = args ? args.roleArn : undefined;
            inputs["stages"] = args ? args.stages : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:codepipeline/pipeline:Pipeline", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Pipeline resources.
 */
export interface PipelineState {
    /**
     * The codepipeline ARN.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * An artifact_store block. Artifact stores are documented below.
     * * `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.
     */
    readonly artifactStore?: pulumi.Input<{ encryptionKey?: pulumi.Input<{ id: pulumi.Input<string>, type: pulumi.Input<string> }>, location: pulumi.Input<string>, type: pulumi.Input<string> }>;
    /**
     * The name of the pipeline.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.
     */
    readonly roleArn?: pulumi.Input<string>;
    readonly stages?: pulumi.Input<pulumi.Input<{ actions: pulumi.Input<pulumi.Input<{ category: pulumi.Input<string>, configuration?: pulumi.Input<{[key: string]: any}>, inputArtifacts?: pulumi.Input<pulumi.Input<string>[]>, name: pulumi.Input<string>, outputArtifacts?: pulumi.Input<pulumi.Input<string>[]>, owner: pulumi.Input<string>, provider: pulumi.Input<string>, roleArn?: pulumi.Input<string>, runOrder?: pulumi.Input<number>, version: pulumi.Input<string> }>[]>, name: pulumi.Input<string> }>[]>;
}

/**
 * The set of arguments for constructing a Pipeline resource.
 */
export interface PipelineArgs {
    /**
     * An artifact_store block. Artifact stores are documented below.
     * * `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.
     */
    readonly artifactStore: pulumi.Input<{ encryptionKey?: pulumi.Input<{ id: pulumi.Input<string>, type: pulumi.Input<string> }>, location: pulumi.Input<string>, type: pulumi.Input<string> }>;
    /**
     * The name of the pipeline.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.
     */
    readonly roleArn: pulumi.Input<string>;
    readonly stages: pulumi.Input<pulumi.Input<{ actions: pulumi.Input<pulumi.Input<{ category: pulumi.Input<string>, configuration?: pulumi.Input<{[key: string]: any}>, inputArtifacts?: pulumi.Input<pulumi.Input<string>[]>, name: pulumi.Input<string>, outputArtifacts?: pulumi.Input<pulumi.Input<string>[]>, owner: pulumi.Input<string>, provider: pulumi.Input<string>, roleArn?: pulumi.Input<string>, runOrder?: pulumi.Input<number>, version: pulumi.Input<string> }>[]>, name: pulumi.Input<string> }>[]>;
}

/**
 * The live Pipeline resource.
 */
export interface PipelineResult {
    /**
     * The codepipeline ARN.
     */
    readonly arn: string;
    /**
     * An artifact_store block. Artifact stores are documented below.
     * * `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.
     */
    readonly artifactStore: { encryptionKey?: { id: string, type: string }, location: string, type: string };
    /**
     * The name of the pipeline.
     */
    readonly name: string;
    /**
     * A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.
     */
    readonly roleArn: string;
    readonly stages: { actions: { category: string, configuration?: {[key: string]: any}, inputArtifacts?: string[], name: string, outputArtifacts?: string[], owner: string, provider: string, roleArn?: string, runOrder: number, version: string }[], name: string }[];
}
