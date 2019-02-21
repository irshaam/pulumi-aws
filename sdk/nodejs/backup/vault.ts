// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides an AWS Backup vault resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.backup.Vault("example", {
 *     kmsKeyArn: aws_kms_key_example.arn,
 * });
 * ```
 */
export class Vault extends pulumi.CustomResource {
    /**
     * Get an existing Vault resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VaultState, opts?: pulumi.CustomResourceOptions): Vault {
        return new Vault(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<VaultResult> {
        return ctx.list({...args, type: 'aws:backup/vault:Vault'});
    }

    /**
     * The ARN of the vault.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The server-side encryption key that is used to protect your backups.
     */
    public readonly kmsKeyArn: pulumi.Output<string>;
    /**
     * Name of the backup vault to create.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The number of recovery points that are stored in a backup vault.
     */
    public /*out*/ readonly recoveryPoints: pulumi.Output<number>;
    /**
     * Metadata that you can assign to help organize the resources that you create.
     */
    public readonly tags: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Vault resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: VaultArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VaultArgs | VaultState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VaultState = argsOrState as VaultState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["kmsKeyArn"] = state ? state.kmsKeyArn : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["recoveryPoints"] = state ? state.recoveryPoints : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as VaultArgs | undefined;
            inputs["kmsKeyArn"] = args ? args.kmsKeyArn : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["recoveryPoints"] = undefined /*out*/;
        }
        super("aws:backup/vault:Vault", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Vault resources.
 */
export interface VaultState {
    /**
     * The ARN of the vault.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The server-side encryption key that is used to protect your backups.
     */
    readonly kmsKeyArn?: pulumi.Input<string>;
    /**
     * Name of the backup vault to create.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The number of recovery points that are stored in a backup vault.
     */
    readonly recoveryPoints?: pulumi.Input<number>;
    /**
     * Metadata that you can assign to help organize the resources that you create.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Vault resource.
 */
export interface VaultArgs {
    /**
     * The server-side encryption key that is used to protect your backups.
     */
    readonly kmsKeyArn?: pulumi.Input<string>;
    /**
     * Name of the backup vault to create.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Metadata that you can assign to help organize the resources that you create.
     */
    readonly tags?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The live Vault resource.
 */
export interface VaultResult {
    /**
     * The ARN of the vault.
     */
    readonly arn: string;
    /**
     * The server-side encryption key that is used to protect your backups.
     */
    readonly kmsKeyArn: string;
    /**
     * Name of the backup vault to create.
     */
    readonly name: string;
    /**
     * The number of recovery points that are stored in a backup vault.
     */
    readonly recoveryPoints: number;
    /**
     * Metadata that you can assign to help organize the resources that you create.
     */
    readonly tags?: {[key: string]: string};
}
