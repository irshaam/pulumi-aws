// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Provides a AWS Transfer User resource. Managing SSH keys can be accomplished with the `aws.transfer.SshKey` resource.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const fooServer = new aws.transfer.Server("fooServer", {
 *     identityProviderType: "SERVICE_MANAGED",
 *     tags: {
 *         NAME: "tf-acc-test-transfer-server",
 *     },
 * });
 * const fooRole = new aws.iam.Role("fooRole", {assumeRolePolicy: `{
 * 	"Version": "2012-10-17",
 * 	"Statement": [
 * 		{
 * 		"Effect": "Allow",
 * 		"Principal": {
 * 			"Service": "transfer.amazonaws.com"
 * 		},
 * 		"Action": "sts:AssumeRole"
 * 		}
 * 	]
 * }
 * `});
 * const fooRolePolicy = new aws.iam.RolePolicy("fooRolePolicy", {
 *     role: fooRole.id,
 *     policy: `{
 * 	"Version": "2012-10-17",
 * 	"Statement": [
 * 		{
 * 			"Sid": "AllowFullAccesstoS3",
 * 			"Effect": "Allow",
 * 			"Action": [
 * 				"s3:*"
 * 			],
 * 			"Resource": "*"
 * 		}
 * 	]
 * }
 * `,
 * });
 * const fooUser = new aws.transfer.User("fooUser", {
 *     serverId: fooServer.id,
 *     userName: "tftestuser",
 *     role: fooRole.arn,
 * });
 * ```
 */
export class User extends pulumi.CustomResource {
    /**
     * Get an existing User resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserState, opts?: pulumi.CustomResourceOptions): User {
        return new User(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:transfer/user:User';

    /**
     * Returns true if the given object is an instance of User.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is User {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === User.__pulumiType;
    }

    /**
     * Amazon Resource Name (ARN) of Transfer User
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
     */
    public readonly homeDirectory!: pulumi.Output<string | undefined>;
    /**
     * Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. documented below.
     */
    public readonly homeDirectoryMappings!: pulumi.Output<outputs.transfer.UserHomeDirectoryMapping[] | undefined>;
    /**
     * The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
     */
    public readonly homeDirectoryType!: pulumi.Output<string | undefined>;
    /**
     * An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. These are evaluated on-the-fly when navigating the bucket.
     */
    public readonly policy!: pulumi.Output<string | undefined>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
     */
    public readonly role!: pulumi.Output<string>;
    /**
     * The Server ID of the Transfer Server (e.g. `s-12345678`)
     */
    public readonly serverId!: pulumi.Output<string>;
    /**
     * A map of tags to assign to the resource.
     */
    public readonly tags!: pulumi.Output<{[key: string]: string} | undefined>;
    /**
     * The name used for log in to your SFTP server.
     */
    public readonly userName!: pulumi.Output<string>;

    /**
     * Create a User resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: UserArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: UserArgs | UserState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as UserState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["homeDirectory"] = state ? state.homeDirectory : undefined;
            inputs["homeDirectoryMappings"] = state ? state.homeDirectoryMappings : undefined;
            inputs["homeDirectoryType"] = state ? state.homeDirectoryType : undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["role"] = state ? state.role : undefined;
            inputs["serverId"] = state ? state.serverId : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["userName"] = state ? state.userName : undefined;
        } else {
            const args = argsOrState as UserArgs | undefined;
            if (!args || args.role === undefined) {
                throw new Error("Missing required property 'role'");
            }
            if (!args || args.serverId === undefined) {
                throw new Error("Missing required property 'serverId'");
            }
            if (!args || args.userName === undefined) {
                throw new Error("Missing required property 'userName'");
            }
            inputs["homeDirectory"] = args ? args.homeDirectory : undefined;
            inputs["homeDirectoryMappings"] = args ? args.homeDirectoryMappings : undefined;
            inputs["homeDirectoryType"] = args ? args.homeDirectoryType : undefined;
            inputs["policy"] = args ? args.policy : undefined;
            inputs["role"] = args ? args.role : undefined;
            inputs["serverId"] = args ? args.serverId : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userName"] = args ? args.userName : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(User.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering User resources.
 */
export interface UserState {
    /**
     * Amazon Resource Name (ARN) of Transfer User
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
     */
    readonly homeDirectory?: pulumi.Input<string>;
    /**
     * Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. documented below.
     */
    readonly homeDirectoryMappings?: pulumi.Input<pulumi.Input<inputs.transfer.UserHomeDirectoryMapping>[]>;
    /**
     * The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
     */
    readonly homeDirectoryType?: pulumi.Input<string>;
    /**
     * An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. These are evaluated on-the-fly when navigating the bucket.
     */
    readonly policy?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
     */
    readonly role?: pulumi.Input<string>;
    /**
     * The Server ID of the Transfer Server (e.g. `s-12345678`)
     */
    readonly serverId?: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The name used for log in to your SFTP server.
     */
    readonly userName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a User resource.
 */
export interface UserArgs {
    /**
     * The landing directory (folder) for a user when they log in to the server using their SFTP client.  It should begin with a `/`.  The first item in the path is the name of the home bucket (accessible as `${Transfer:HomeBucket}` in the policy) and the rest is the home directory (accessible as `${Transfer:HomeDirectory}` in the policy). For example, `/example-bucket-1234/username` would set the home bucket to `example-bucket-1234` and the home directory to `username`.
     */
    readonly homeDirectory?: pulumi.Input<string>;
    /**
     * Logical directory mappings that specify what S3 paths and keys should be visible to your user and how you want to make them visible. documented below.
     */
    readonly homeDirectoryMappings?: pulumi.Input<pulumi.Input<inputs.transfer.UserHomeDirectoryMapping>[]>;
    /**
     * The type of landing directory (folder) you mapped for your users' home directory. Valid values are `PATH` and `LOGICAL`.
     */
    readonly homeDirectoryType?: pulumi.Input<string>;
    /**
     * An IAM JSON policy document that scopes down user access to portions of their Amazon S3 bucket. IAM variables you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`. These are evaluated on-the-fly when navigating the bucket.
     */
    readonly policy?: pulumi.Input<string>;
    /**
     * Amazon Resource Name (ARN) of an IAM role that allows the service to controls your user’s access to your Amazon S3 bucket.
     */
    readonly role: pulumi.Input<string>;
    /**
     * The Server ID of the Transfer Server (e.g. `s-12345678`)
     */
    readonly serverId: pulumi.Input<string>;
    /**
     * A map of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
    /**
     * The name used for log in to your SFTP server.
     */
    readonly userName: pulumi.Input<string>;
}
