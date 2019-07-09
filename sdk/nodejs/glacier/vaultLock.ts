// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

export class VaultLock extends pulumi.CustomResource {
    /**
     * Get an existing VaultLock resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VaultLockState, opts?: pulumi.CustomResourceOptions): VaultLock {
        return new VaultLock(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws:glacier/vaultLock:VaultLock';

    /**
     * Returns true if the given object is an instance of VaultLock.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VaultLock {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VaultLock.__pulumiType;
    }

    public readonly completeLock!: pulumi.Output<boolean>;
    public readonly ignoreDeletionError!: pulumi.Output<boolean | undefined>;
    /**
     * JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
     */
    public readonly policy!: pulumi.Output<string>;
    /**
     * The name of the Glacier Vault.
     */
    public readonly vaultName!: pulumi.Output<string>;

    /**
     * Create a VaultLock resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VaultLockArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VaultLockArgs | VaultLockState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VaultLockState | undefined;
            inputs["completeLock"] = state ? state.completeLock : undefined;
            inputs["ignoreDeletionError"] = state ? state.ignoreDeletionError : undefined;
            inputs["policy"] = state ? state.policy : undefined;
            inputs["vaultName"] = state ? state.vaultName : undefined;
        } else {
            const args = argsOrState as VaultLockArgs | undefined;
            if (!args || args.completeLock === undefined) {
                throw new Error("Missing required property 'completeLock'");
            }
            if (!args || args.policy === undefined) {
                throw new Error("Missing required property 'policy'");
            }
            if (!args || args.vaultName === undefined) {
                throw new Error("Missing required property 'vaultName'");
            }
            inputs["completeLock"] = args ? args.completeLock : undefined;
            inputs["ignoreDeletionError"] = args ? args.ignoreDeletionError : undefined;
            inputs["policy"] = args ? args.policy : undefined;
            inputs["vaultName"] = args ? args.vaultName : undefined;
        }
        super(VaultLock.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VaultLock resources.
 */
export interface VaultLockState {
    readonly completeLock?: pulumi.Input<boolean>;
    readonly ignoreDeletionError?: pulumi.Input<boolean>;
    /**
     * JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
     */
    readonly policy?: pulumi.Input<string>;
    /**
     * The name of the Glacier Vault.
     */
    readonly vaultName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VaultLock resource.
 */
export interface VaultLockArgs {
    readonly completeLock: pulumi.Input<boolean>;
    readonly ignoreDeletionError?: pulumi.Input<boolean>;
    /**
     * JSON string containing the IAM policy to apply as the Glacier Vault Lock policy.
     */
    readonly policy: pulumi.Input<string>;
    /**
     * The name of the Glacier Vault.
     */
    readonly vaultName: pulumi.Input<string>;
}
