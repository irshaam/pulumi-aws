// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Kms
{
    public static class GetKey
    {
        /// <summary>
        /// Use this data source to get detailed information about
        /// the specified KMS Key with flexible key id input.
        /// This can be useful to reference key alias
        /// without having to hard code the ARN as input.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Aws = Pulumi.Aws;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var byAlias = Output.Create(Aws.Kms.GetKey.InvokeAsync(new Aws.Kms.GetKeyArgs
        ///         {
        ///             KeyId = "alias/my-key",
        ///         }));
        ///         var byId = Output.Create(Aws.Kms.GetKey.InvokeAsync(new Aws.Kms.GetKeyArgs
        ///         {
        ///             KeyId = "1234abcd-12ab-34cd-56ef-1234567890ab",
        ///         }));
        ///         var byAliasArn = Output.Create(Aws.Kms.GetKey.InvokeAsync(new Aws.Kms.GetKeyArgs
        ///         {
        ///             KeyId = "arn:aws:kms:us-east-1:111122223333:alias/my-key",
        ///         }));
        ///         var byKeyArn = Output.Create(Aws.Kms.GetKey.InvokeAsync(new Aws.Kms.GetKeyArgs
        ///         {
        ///             KeyId = "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetKeyResult> InvokeAsync(GetKeyArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetKeyResult>("aws:kms/getKey:getKey", args ?? new GetKeyArgs(), options.WithVersion());
    }


    public sealed class GetKeyArgs : Pulumi.InvokeArgs
    {
        [Input("grantTokens")]
        private List<string>? _grantTokens;

        /// <summary>
        /// List of grant tokens
        /// </summary>
        public List<string> GrantTokens
        {
            get => _grantTokens ?? (_grantTokens = new List<string>());
            set => _grantTokens = value;
        }

        /// <summary>
        /// Key identifier which can be one of the following format:
        /// * Key ID. E.g: `1234abcd-12ab-34cd-56ef-1234567890ab`
        /// * Key ARN. E.g.: `arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
        /// * Alias name. E.g.: `alias/my-key`
        /// * Alias ARN: E.g.: `arn:aws:kms:us-east-1:111122223333:alias/my-key`
        /// </summary>
        [Input("keyId", required: true)]
        public string KeyId { get; set; } = null!;

        public GetKeyArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetKeyResult
    {
        public readonly string Arn;
        public readonly string AwsAccountId;
        public readonly string CreationDate;
        public readonly string CustomerMasterKeySpec;
        public readonly string DeletionDate;
        public readonly string Description;
        public readonly bool Enabled;
        public readonly string ExpirationModel;
        public readonly ImmutableArray<string> GrantTokens;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string KeyId;
        public readonly string KeyManager;
        public readonly string KeyState;
        public readonly string KeyUsage;
        public readonly string Origin;
        public readonly string ValidTo;

        [OutputConstructor]
        private GetKeyResult(
            string arn,

            string awsAccountId,

            string creationDate,

            string customerMasterKeySpec,

            string deletionDate,

            string description,

            bool enabled,

            string expirationModel,

            ImmutableArray<string> grantTokens,

            string id,

            string keyId,

            string keyManager,

            string keyState,

            string keyUsage,

            string origin,

            string validTo)
        {
            Arn = arn;
            AwsAccountId = awsAccountId;
            CreationDate = creationDate;
            CustomerMasterKeySpec = customerMasterKeySpec;
            DeletionDate = deletionDate;
            Description = description;
            Enabled = enabled;
            ExpirationModel = expirationModel;
            GrantTokens = grantTokens;
            Id = id;
            KeyId = keyId;
            KeyManager = keyManager;
            KeyState = keyState;
            KeyUsage = keyUsage;
            Origin = origin;
            ValidTo = validTo;
        }
    }
}
