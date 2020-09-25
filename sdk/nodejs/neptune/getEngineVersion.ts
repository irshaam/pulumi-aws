// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Information about a Neptune engine version.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 *
 * const test = pulumi.output(aws.neptune.getEngineVersion({
 *     preferredVersions: [
 *         "1.0.3.0",
 *         "1.0.2.2",
 *         "1.0.2.1",
 *     ],
 * }, { async: true }));
 * ```
 */
export function getEngineVersion(args?: GetEngineVersionArgs, opts?: pulumi.InvokeOptions): Promise<GetEngineVersionResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("aws:neptune/getEngineVersion:getEngineVersion", {
        "engine": args.engine,
        "parameterGroupFamily": args.parameterGroupFamily,
        "preferredVersions": args.preferredVersions,
        "version": args.version,
    }, opts);
}

/**
 * A collection of arguments for invoking getEngineVersion.
 */
export interface GetEngineVersionArgs {
    /**
     * DB engine. (Default: `neptune`)
     */
    readonly engine?: string;
    /**
     * The name of a specific DB parameter group family. An example parameter group family is `neptune1`.
     */
    readonly parameterGroupFamily?: string;
    /**
     * Ordered list of preferred engine versions. The first match in this list will be returned. If no preferred matches are found and the original search returned more than one result, an error is returned. If both the `version` and `preferredVersions` arguments are not configured, the data source will return the default version for the engine.
     */
    readonly preferredVersions?: string[];
    /**
     * Version of the DB engine. For example, `1.0.1.0`, `1.0.2.2`, and `1.0.3.0`. If both the `version` and `preferredVersions` arguments are not configured, the data source will return the default version for the engine.
     */
    readonly version?: string;
}

/**
 * A collection of values returned by getEngineVersion.
 */
export interface GetEngineVersionResult {
    readonly engine?: string;
    /**
     * The description of the database engine.
     */
    readonly engineDescription: string;
    /**
     * Set of log types that the database engine has available for export to CloudWatch Logs.
     */
    readonly exportableLogTypes: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly parameterGroupFamily: string;
    readonly preferredVersions?: string[];
    /**
     * Set of the time zones supported by this engine.
     */
    readonly supportedTimezones: string[];
    /**
     * Indicates whether the engine version supports exporting the log types specified by `exportableLogTypes` to CloudWatch Logs.
     */
    readonly supportsLogExportsToCloudwatch: boolean;
    /**
     * Indicates whether the database engine version supports read replicas.
     */
    readonly supportsReadReplica: boolean;
    /**
     * Set of engine versions that this database engine version can be upgraded to.
     */
    readonly validUpgradeTargets: string[];
    readonly version: string;
    /**
     * The description of the database engine version.
     */
    readonly versionDescription: string;
}
