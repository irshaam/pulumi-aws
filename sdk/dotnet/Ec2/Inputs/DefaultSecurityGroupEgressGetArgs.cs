// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ec2.Inputs
{

    public sealed class DefaultSecurityGroupEgressGetArgs : Pulumi.ResourceArgs
    {
        [Input("cidrBlocks")]
        private InputList<string>? _cidrBlocks;

        /// <summary>
        /// List of CIDR blocks.
        /// </summary>
        public InputList<string> CidrBlocks
        {
            get => _cidrBlocks ?? (_cidrBlocks = new InputList<string>());
            set => _cidrBlocks = value;
        }

        /// <summary>
        /// Description of this egress rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The start port (or ICMP type number if protocol is "icmp")
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        [Input("ipv6CidrBlocks")]
        private InputList<string>? _ipv6CidrBlocks;

        /// <summary>
        /// List of IPv6 CIDR blocks.
        /// </summary>
        public InputList<string> Ipv6CidrBlocks
        {
            get => _ipv6CidrBlocks ?? (_ipv6CidrBlocks = new InputList<string>());
            set => _ipv6CidrBlocks = value;
        }

        [Input("prefixListIds")]
        private InputList<string>? _prefixListIds;

        /// <summary>
        /// List of prefix list IDs (for allowing access to VPC endpoints)
        /// </summary>
        public InputList<string> PrefixListIds
        {
            get => _prefixListIds ?? (_prefixListIds = new InputList<string>());
            set => _prefixListIds = value;
        }

        /// <summary>
        /// The protocol. If you select a protocol of "-1" (semantically equivalent to `"all"`, which is not a valid value here), you must specify a "from_port" and "to_port" equal to 0. If not icmp, tcp, udp, or "-1" use the [protocol number](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml)
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// List of security group Group Names if using EC2-Classic, or Group IDs if using a VPC.
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// If true, the security group itself will be added as a source to this egress rule.
        /// </summary>
        [Input("self")]
        public Input<bool>? Self { get; set; }

        /// <summary>
        /// The end range port (or ICMP code if protocol is "icmp").
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public DefaultSecurityGroupEgressGetArgs()
        {
        }
    }
}
