// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * Provides an SES domain identity resource
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const example = new aws.ses.DomainIdentity("example", {
 *     domain: "example.com",
 * });
 * const exampleAmazonsesVerificationRecord = new aws.route53.Record("example_amazonses_verification_record", {
 *     records: [example.verificationToken],
 *     ttl: 600,
 *     type: "TXT",
 *     zoneId: "ABCDEFGHIJ123",
 * });
 * ```
 */
export class DomainIdentity extends pulumi.CustomResource {
    /**
     * Get an existing DomainIdentity resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainIdentityState, opts?: pulumi.CustomResourceOptions): DomainIdentity {
        return new DomainIdentity(name, <any>state, { ...opts, id: id });
    }

    public static list(ctx: pulumi.query.ListContext, args?: pulumi.query.ListArgs): rxjs.Observable<DomainIdentityResult> {
        return ctx.list({...args, type: 'aws:ses/domainIdentity:DomainIdentity'});
    }

    /**
     * The ARN of the domain identity.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The domain name to assign to SES
     */
    public readonly domain: pulumi.Output<string>;
    /**
     * A code which when added to the domain as a TXT record
     * will signal to SES that the owner of the domain has authorised SES to act on
     * their behalf. The domain identity will be in state "verification pending"
     * until this is done. See below for an example of how this might be achieved
     * when the domain is hosted in Route 53 and managed by Terraform.  Find out
     * more about verifying domains in Amazon SES in the [AWS SES
     * docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
     */
    public /*out*/ readonly verificationToken: pulumi.Output<string>;

    /**
     * Create a DomainIdentity resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainIdentityArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DomainIdentityArgs | DomainIdentityState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DomainIdentityState = argsOrState as DomainIdentityState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["domain"] = state ? state.domain : undefined;
            inputs["verificationToken"] = state ? state.verificationToken : undefined;
        } else {
            const args = argsOrState as DomainIdentityArgs | undefined;
            if (!args || args.domain === undefined) {
                throw new Error("Missing required property 'domain'");
            }
            inputs["domain"] = args ? args.domain : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["verificationToken"] = undefined /*out*/;
        }
        super("aws:ses/domainIdentity:DomainIdentity", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DomainIdentity resources.
 */
export interface DomainIdentityState {
    /**
     * The ARN of the domain identity.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The domain name to assign to SES
     */
    readonly domain?: pulumi.Input<string>;
    /**
     * A code which when added to the domain as a TXT record
     * will signal to SES that the owner of the domain has authorised SES to act on
     * their behalf. The domain identity will be in state "verification pending"
     * until this is done. See below for an example of how this might be achieved
     * when the domain is hosted in Route 53 and managed by Terraform.  Find out
     * more about verifying domains in Amazon SES in the [AWS SES
     * docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
     */
    readonly verificationToken?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DomainIdentity resource.
 */
export interface DomainIdentityArgs {
    /**
     * The domain name to assign to SES
     */
    readonly domain: pulumi.Input<string>;
}

/**
 * The live DomainIdentity resource.
 */
export interface DomainIdentityResult {
    /**
     * The ARN of the domain identity.
     */
    readonly arn: string;
    /**
     * The domain name to assign to SES
     */
    readonly domain: string;
    /**
     * A code which when added to the domain as a TXT record
     * will signal to SES that the owner of the domain has authorised SES to act on
     * their behalf. The domain identity will be in state "verification pending"
     * until this is done. See below for an example of how this might be achieved
     * when the domain is hosted in Route 53 and managed by Terraform.  Find out
     * more about verifying domains in Amazon SES in the [AWS SES
     * docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
     */
    readonly verificationToken: string;
}
