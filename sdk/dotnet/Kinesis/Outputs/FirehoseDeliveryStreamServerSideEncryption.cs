// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Kinesis.Outputs
{

    [OutputType]
    public sealed class FirehoseDeliveryStreamServerSideEncryption
    {
        /// <summary>
        /// Whether to enable encryption at rest. Default is `false`.
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// Amazon Resource Name (ARN) of the encryption key. Required when `key_type` is `CUSTOMER_MANAGED_CMK`.
        /// </summary>
        public readonly string? KeyArn;
        /// <summary>
        /// Type of encryption key. Default is `AWS_OWNED_CMK`. Valid values are `AWS_OWNED_CMK` and `CUSTOMER_MANAGED_CMK`
        /// </summary>
        public readonly string? KeyType;

        [OutputConstructor]
        private FirehoseDeliveryStreamServerSideEncryption(
            bool? enabled,

            string? keyArn,

            string? keyType)
        {
            Enabled = enabled;
            KeyArn = keyArn;
            KeyType = keyType;
        }
    }
}
