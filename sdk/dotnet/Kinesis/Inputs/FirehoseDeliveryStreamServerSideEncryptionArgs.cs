// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Kinesis.Inputs
{

    public sealed class FirehoseDeliveryStreamServerSideEncryptionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to enable encryption at rest. Default is `false`.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// Amazon Resource Name (ARN) of the encryption key. Required when `key_type` is `CUSTOMER_MANAGED_CMK`.
        /// </summary>
        [Input("keyArn")]
        public Input<string>? KeyArn { get; set; }

        /// <summary>
        /// Type of encryption key. Default is `AWS_OWNED_CMK`. Valid values are `AWS_OWNED_CMK` and `CUSTOMER_MANAGED_CMK`
        /// </summary>
        [Input("keyType")]
        public Input<string>? KeyType { get; set; }

        public FirehoseDeliveryStreamServerSideEncryptionArgs()
        {
        }
    }
}
