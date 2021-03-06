// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.WafV2.Inputs
{

    public sealed class WebAclRuleActionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Instructs AWS WAF to allow the web request. Configure as an empty block `{}`.
        /// </summary>
        [Input("allow")]
        public Input<Inputs.WebAclRuleActionAllowArgs>? Allow { get; set; }

        /// <summary>
        /// Instructs AWS WAF to block the web request. Configure as an empty block `{}`.
        /// </summary>
        [Input("block")]
        public Input<Inputs.WebAclRuleActionBlockArgs>? Block { get; set; }

        /// <summary>
        /// Instructs AWS WAF to count the web request and allow it. Configure as an empty block `{}`.
        /// </summary>
        [Input("count")]
        public Input<Inputs.WebAclRuleActionCountArgs>? Count { get; set; }

        public WebAclRuleActionArgs()
        {
        }
    }
}
