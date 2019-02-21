// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Uploads an SSH public key and associates it with the specified IAM user.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const userUser = new aws.iam.User("user", {
 *     path: "/",
 * });
 * const userSshKey = new aws.iam.SshKey("user", {
 *     encoding: "SSH",
 *     publicKey: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD3F6tyPEFEzV0LX3X8BsXdMsQz1x2cEikKDEY0aIj41qgxMCP/iteneqXSIFZBp5vizPvaoIR3Um9xK7PGoW8giupGn+EPuxIA4cDM4vzOqOkiMPhz5XK0whEjkVzTo4+S0puvDZuwIsdiW9mxhJc7tgBNL0cYlWSYVkz4G/fslNfRPW5mYAM49f4fhtxPb5ok4Q2Lg9dPKVHO/Bgeu5woMc7RY0p1ej6D4CKFE6lymSDJpW0YHX/wqE9+cfEauh7xZcG0q9t2ta6F6fmX0agvpFyZo8aFbXeUBr7osSCJNgvavWbM/06niWrOvYX2xwWdhXmXSrbX8ZbabVohBK41 mytest@mydomain.com",
 *     username: userUser.name,
 * });
 * ```
 */
export class SshKey extends pulumi.CustomResource {
    /**
     * Get an existing SshKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SshKeyState, opts?: pulumi.CustomResourceOptions): SshKey {
        return new SshKey(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<SshKeyResult> {
        return ctx.list({...args, type: 'aws:iam/sshKey:SshKey'});
    }

    /**
     * Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
     */
    public readonly encoding: pulumi.Output<string>;
    /**
     * The MD5 message digest of the SSH public key.
     */
    public /*out*/ readonly fingerprint: pulumi.Output<string>;
    /**
     * The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
     */
    public readonly publicKey: pulumi.Output<string>;
    /**
     * The unique identifier for the SSH public key.
     */
    public /*out*/ readonly sshPublicKeyId: pulumi.Output<string>;
    /**
     * The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
     */
    public readonly status: pulumi.Output<string>;
    /**
     * The name of the IAM user to associate the SSH public key with.
     */
    public readonly username: pulumi.Output<string>;

    /**
     * Create a SshKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SshKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SshKeyArgs | SshKeyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SshKeyState = argsOrState as SshKeyState | undefined;
            inputs["encoding"] = state ? state.encoding : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["publicKey"] = state ? state.publicKey : undefined;
            inputs["sshPublicKeyId"] = state ? state.sshPublicKeyId : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["username"] = state ? state.username : undefined;
        } else {
            const args = argsOrState as SshKeyArgs | undefined;
            if (!args || args.encoding === undefined) {
                throw new Error("Missing required property 'encoding'");
            }
            if (!args || args.publicKey === undefined) {
                throw new Error("Missing required property 'publicKey'");
            }
            if (!args || args.username === undefined) {
                throw new Error("Missing required property 'username'");
            }
            inputs["encoding"] = args ? args.encoding : undefined;
            inputs["publicKey"] = args ? args.publicKey : undefined;
            inputs["status"] = args ? args.status : undefined;
            inputs["username"] = args ? args.username : undefined;
            inputs["fingerprint"] = undefined /*out*/;
            inputs["sshPublicKeyId"] = undefined /*out*/;
        }
        super("aws:iam/sshKey:SshKey", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SshKey resources.
 */
export interface SshKeyState {
    /**
     * Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
     */
    readonly encoding?: pulumi.Input<string>;
    /**
     * The MD5 message digest of the SSH public key.
     */
    readonly fingerprint?: pulumi.Input<string>;
    /**
     * The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
     */
    readonly publicKey?: pulumi.Input<string>;
    /**
     * The unique identifier for the SSH public key.
     */
    readonly sshPublicKeyId?: pulumi.Input<string>;
    /**
     * The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The name of the IAM user to associate the SSH public key with.
     */
    readonly username?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SshKey resource.
 */
export interface SshKeyArgs {
    /**
     * Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
     */
    readonly encoding: pulumi.Input<string>;
    /**
     * The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
     */
    readonly publicKey: pulumi.Input<string>;
    /**
     * The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * The name of the IAM user to associate the SSH public key with.
     */
    readonly username: pulumi.Input<string>;
}

/**
 * The live SshKey resource.
 */
export interface SshKeyResult {
    /**
     * Specifies the public key encoding format to use in the response. To retrieve the public key in ssh-rsa format, use `SSH`. To retrieve the public key in PEM format, use `PEM`.
     */
    readonly encoding: string;
    /**
     * The MD5 message digest of the SSH public key.
     */
    readonly fingerprint: string;
    /**
     * The SSH public key. The public key must be encoded in ssh-rsa format or PEM format.
     */
    readonly publicKey: string;
    /**
     * The unique identifier for the SSH public key.
     */
    readonly sshPublicKeyId: string;
    /**
     * The status to assign to the SSH public key. Active means the key can be used for authentication with an AWS CodeCommit repository. Inactive means the key cannot be used. Default is `active`.
     */
    readonly status: string;
    /**
     * The name of the IAM user to associate the SSH public key with.
     */
    readonly username: string;
}
