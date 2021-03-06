// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2.Inputs
{

    public sealed class LaunchTemplateBlockDeviceMappingEbsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether the volume should be destroyed on instance termination. Defaults to `false` if not set. See [Preserving Amazon EBS Volumes on Instance Termination](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#preserving-volumes-on-termination) for more information.
        /// </summary>
        [Input("deleteOnTermination")]
        public Input<string>? DeleteOnTermination { get; set; }

        /// <summary>
        /// Enables [EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
        /// on the volume (Default: `false`). Cannot be used with `snapshot_id`.
        /// </summary>
        [Input("encrypted")]
        public Input<string>? Encrypted { get; set; }

        /// <summary>
        /// The amount of provisioned
        /// [IOPS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
        /// This must be set with a `volume_type` of `"io1/io2"`.
        /// </summary>
        [Input("iops")]
        public Input<int>? Iops { get; set; }

        /// <summary>
        /// The ARN of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use when creating the encrypted volume.
        /// `encrypted` must be set to `true` when this is set.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The Snapshot ID to mount.
        /// </summary>
        [Input("snapshotId")]
        public Input<string>? SnapshotId { get; set; }

        /// <summary>
        /// The size of the volume in gigabytes.
        /// </summary>
        [Input("volumeSize")]
        public Input<int>? VolumeSize { get; set; }

        /// <summary>
        /// The type of volume. Can be `"standard"`, `"gp2"`, `"io1"` or `"io2"`. (Default: `"standard"`).
        /// </summary>
        [Input("volumeType")]
        public Input<string>? VolumeType { get; set; }

        public LaunchTemplateBlockDeviceMappingEbsGetArgs()
        {
        }
    }
}
