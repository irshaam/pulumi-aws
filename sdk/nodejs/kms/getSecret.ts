// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";
import * as rxjs from "rxjs";
import * as operators from "rxjs/operators";

/**
 * !> **WARNING:** This data source is deprecated and will be removed in the next major version. You can migrate existing configurations to the [`aws_kms_secrets` data source](https://www.terraform.io/docs/providers/aws/d/kms_secrets.html) following instructions available in the [Version 2 Upgrade Guide](https://www.terraform.io/docs/providers/aws/guides/version-2-upgrade.html#data-source-aws_kms_secret).
 * 
 * The KMS secret data source allows you to use data encrypted with the AWS KMS
 * service within your resource definitions.
 * 
 * > **NOTE**: Using this data provider will allow you to conceal secret data within your
 * resource definitions but does not take care of protecting that data in the
 * logging output, plan output or state output.
 * 
 * Please take care to secure your secret data outside of resource definitions.
 */
export function getSecret(args: GetSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretResult> {
    return pulumi.runtime.invoke("aws:kms/getSecret:getSecret", {
        "__hasDynamicAttributes": args.__hasDynamicAttributes,
        "secrets": args.secrets,
    }, opts);
}

/**
 * A collection of arguments for invoking getSecret.
 */
export interface GetSecretArgs {
    readonly __hasDynamicAttributes?: string;
    /**
     * One or more encrypted payload definitions from the KMS
     * service.  See the Secret Definitions below.
     */
    readonly secrets: { context?: {[key: string]: string}, grantTokens?: string[], name: string, payload: string }[];
}

/**
 * A collection of values returned by getSecret.
 */
export interface GetSecretResult {
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
