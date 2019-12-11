// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Aws.Ssm
{
    /// <summary>
    /// Provides an SSM Document resource
    /// 
    /// &gt; **NOTE on updating SSM documents:** Only documents with a schema version of 2.0
    /// or greater can update their content once created, see [SSM Schema Features][1]. To update a document with an older
    /// schema version you must recreate the resource.
    /// 
    /// ## Permissions
    /// 
    /// The permissions attribute specifies how you want to share the document. If you share a document privately,
    /// you must specify the AWS user account IDs for those people who can use the document. If you share a document
    /// publicly, you must specify All as the account ID.
    /// 
    /// The permissions mapping supports the following:
    /// 
    /// * `type` - The permission type for the document. The permission type can be `Share`.
    /// * `account_ids` - The AWS user accounts that should have access to the document. The account IDs can either be a group of account IDs or `All`.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_document.html.markdown.
    /// </summary>
    public partial class Document : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The JSON or YAML content of the document.
        /// </summary>
        [Output("content")]
        public Output<string> Content { get; private set; } = null!;

        /// <summary>
        /// The date the document was created.
        /// </summary>
        [Output("createdDate")]
        public Output<string> CreatedDate { get; private set; } = null!;

        /// <summary>
        /// The default version of the document.
        /// </summary>
        [Output("defaultVersion")]
        public Output<string> DefaultVersion { get; private set; } = null!;

        /// <summary>
        /// The description of the document.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The format of the document. Valid document types include: `JSON` and `YAML`
        /// </summary>
        [Output("documentFormat")]
        public Output<string?> DocumentFormat { get; private set; } = null!;

        /// <summary>
        /// The type of the document. Valid document types include: `Command`, `Policy`, `Automation` and `Session`
        /// </summary>
        [Output("documentType")]
        public Output<string> DocumentType { get; private set; } = null!;

        /// <summary>
        /// The sha1 or sha256 of the document content
        /// </summary>
        [Output("hash")]
        public Output<string> Hash { get; private set; } = null!;

        /// <summary>
        /// "Sha1" "Sha256". The hashing algorithm used when hashing the content.
        /// </summary>
        [Output("hashType")]
        public Output<string> HashType { get; private set; } = null!;

        /// <summary>
        /// The latest version of the document.
        /// </summary>
        [Output("latestVersion")]
        public Output<string> LatestVersion { get; private set; } = null!;

        /// <summary>
        /// The name of the document.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The AWS user account of the person who created the document.
        /// </summary>
        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        /// <summary>
        /// The parameters that are available to this document.
        /// </summary>
        [Output("parameters")]
        public Output<ImmutableArray<Outputs.DocumentParameters>> Parameters { get; private set; } = null!;

        /// <summary>
        /// Additional Permissions to attach to the document. See Permissions below for details.
        /// </summary>
        [Output("permissions")]
        public Output<Outputs.DocumentPermissions?> Permissions { get; private set; } = null!;

        /// <summary>
        /// A list of OS platforms compatible with this SSM document, either "Windows" or "Linux".
        /// </summary>
        [Output("platformTypes")]
        public Output<ImmutableArray<string>> PlatformTypes { get; private set; } = null!;

        /// <summary>
        /// The schema version of the document.
        /// </summary>
        [Output("schemaVersion")]
        public Output<string> SchemaVersion { get; private set; } = null!;

        /// <summary>
        /// "Creating", "Active" or "Deleting". The current status of the document.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// A mapping of tags to assign to the object.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableDictionary<string, object>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Document resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Document(string name, DocumentArgs args, CustomResourceOptions? options = null)
            : base("aws:ssm/document:Document", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Document(string name, Input<string> id, DocumentState? state = null, CustomResourceOptions? options = null)
            : base("aws:ssm/document:Document", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Document resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Document Get(string name, Input<string> id, DocumentState? state = null, CustomResourceOptions? options = null)
        {
            return new Document(name, id, state, options);
        }
    }

    public sealed class DocumentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The JSON or YAML content of the document.
        /// </summary>
        [Input("content", required: true)]
        public Input<string> Content { get; set; } = null!;

        /// <summary>
        /// The format of the document. Valid document types include: `JSON` and `YAML`
        /// </summary>
        [Input("documentFormat")]
        public Input<string>? DocumentFormat { get; set; }

        /// <summary>
        /// The type of the document. Valid document types include: `Command`, `Policy`, `Automation` and `Session`
        /// </summary>
        [Input("documentType", required: true)]
        public Input<string> DocumentType { get; set; } = null!;

        /// <summary>
        /// The name of the document.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Additional Permissions to attach to the document. See Permissions below for details.
        /// </summary>
        [Input("permissions")]
        public Input<Inputs.DocumentPermissionsArgs>? Permissions { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the object.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public DocumentArgs()
        {
        }
    }

    public sealed class DocumentState : Pulumi.ResourceArgs
    {
        [Input("arn")]
        public Input<string>? Arn { get; set; }

        /// <summary>
        /// The JSON or YAML content of the document.
        /// </summary>
        [Input("content")]
        public Input<string>? Content { get; set; }

        /// <summary>
        /// The date the document was created.
        /// </summary>
        [Input("createdDate")]
        public Input<string>? CreatedDate { get; set; }

        /// <summary>
        /// The default version of the document.
        /// </summary>
        [Input("defaultVersion")]
        public Input<string>? DefaultVersion { get; set; }

        /// <summary>
        /// The description of the document.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The format of the document. Valid document types include: `JSON` and `YAML`
        /// </summary>
        [Input("documentFormat")]
        public Input<string>? DocumentFormat { get; set; }

        /// <summary>
        /// The type of the document. Valid document types include: `Command`, `Policy`, `Automation` and `Session`
        /// </summary>
        [Input("documentType")]
        public Input<string>? DocumentType { get; set; }

        /// <summary>
        /// The sha1 or sha256 of the document content
        /// </summary>
        [Input("hash")]
        public Input<string>? Hash { get; set; }

        /// <summary>
        /// "Sha1" "Sha256". The hashing algorithm used when hashing the content.
        /// </summary>
        [Input("hashType")]
        public Input<string>? HashType { get; set; }

        /// <summary>
        /// The latest version of the document.
        /// </summary>
        [Input("latestVersion")]
        public Input<string>? LatestVersion { get; set; }

        /// <summary>
        /// The name of the document.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The AWS user account of the person who created the document.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("parameters")]
        private InputList<Inputs.DocumentParametersGetArgs>? _parameters;

        /// <summary>
        /// The parameters that are available to this document.
        /// </summary>
        public InputList<Inputs.DocumentParametersGetArgs> Parameters
        {
            get => _parameters ?? (_parameters = new InputList<Inputs.DocumentParametersGetArgs>());
            set => _parameters = value;
        }

        /// <summary>
        /// Additional Permissions to attach to the document. See Permissions below for details.
        /// </summary>
        [Input("permissions")]
        public Input<Inputs.DocumentPermissionsGetArgs>? Permissions { get; set; }

        [Input("platformTypes")]
        private InputList<string>? _platformTypes;

        /// <summary>
        /// A list of OS platforms compatible with this SSM document, either "Windows" or "Linux".
        /// </summary>
        public InputList<string> PlatformTypes
        {
            get => _platformTypes ?? (_platformTypes = new InputList<string>());
            set => _platformTypes = value;
        }

        /// <summary>
        /// The schema version of the document.
        /// </summary>
        [Input("schemaVersion")]
        public Input<string>? SchemaVersion { get; set; }

        /// <summary>
        /// "Creating", "Active" or "Deleting". The current status of the document.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputMap<object>? _tags;

        /// <summary>
        /// A mapping of tags to assign to the object.
        /// </summary>
        public InputMap<object> Tags
        {
            get => _tags ?? (_tags = new InputMap<object>());
            set => _tags = value;
        }

        public DocumentState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class DocumentParametersGetArgs : Pulumi.ResourceArgs
    {
        [Input("defaultValue")]
        public Input<string>? DefaultValue { get; set; }

        /// <summary>
        /// The description of the document.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the document.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("type")]
        public Input<string>? Type { get; set; }

        public DocumentParametersGetArgs()
        {
        }
    }

    public sealed class DocumentPermissionsArgs : Pulumi.ResourceArgs
    {
        [Input("accountIds", required: true)]
        public Input<string> AccountIds { get; set; } = null!;

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DocumentPermissionsArgs()
        {
        }
    }

    public sealed class DocumentPermissionsGetArgs : Pulumi.ResourceArgs
    {
        [Input("accountIds", required: true)]
        public Input<string> AccountIds { get; set; } = null!;

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public DocumentPermissionsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class DocumentParameters
    {
        public readonly string? DefaultValue;
        /// <summary>
        /// The description of the document.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The name of the document.
        /// </summary>
        public readonly string? Name;
        public readonly string? Type;

        [OutputConstructor]
        private DocumentParameters(
            string? defaultValue,
            string? description,
            string? name,
            string? type)
        {
            DefaultValue = defaultValue;
            Description = description;
            Name = name;
            Type = type;
        }
    }

    [OutputType]
    public sealed class DocumentPermissions
    {
        public readonly string AccountIds;
        public readonly string Type;

        [OutputConstructor]
        private DocumentPermissions(
            string accountIds,
            string type)
        {
            AccountIds = accountIds;
            Type = type;
        }
    }
    }
}
