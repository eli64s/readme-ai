
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
xmpp-rs
</h1>
<h3 align="center">📍 Git xmpp-rs: Developing Your XMPP Solution with Rust".</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/C-A8B9CC.svg?style=for-the-badge&logo=C&logoColor=black" alt="" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="rs" />
<img src="https://img.shields.io/badge/SVG-FFB13B.svg?style=for-the-badge&logo=SVG&logoColor=black" alt="c" />
<img src="https://img.shields.io/badge/Rust-000000.svg?style=for-the-badge&logo=Rust&logoColor=white" alt="pack" />
</p>

</div>

---

## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---


## 📍Overview

Git project xmpp-rs is an open source Rust library providing an API and implementation for the XMPP protocol. It offers a full implementation, providing a complete set of features for network communications, messaging, presence, and error reporting. Additionally, it also supports a wide variety of XMPP extensions, making it a

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---


<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure


```bash
repo
├── Cargo.toml
├── LICENSE
├── README.md
├── icu
│   ├── Cargo.toml
│   ├── build.rs
│   └── src
│       ├── bindings.c
│       ├── bindings.rs
│       ├── error.rs
│       ├── idna2008.rs
│       ├── lib.rs
│       ├── spoof.rs
│       └── stringprep.rs
├── jid
│   ├── CHANGELOG.md
│   ├── Cargo.toml
│   ├── LICENSE
│   ├── README.md
│   └── src
│       └── lib.rs
├── minidom
│   ├── CHANGELOG.md
│   ├── Cargo.toml
│   ├── LICENSE
│   ├── README.md
│   ├── examples
│   │   └── articles.rs
│   └── src
│       ├── convert.rs
│       ├── element.rs
│       ├── error.rs
│       ├── lib.rs
│       ├── namespaces.rs
│       ├── node.rs
│       ├── prefixes.rs
│       ├── tests.rs
│       └── tree_builder.rs
├── parsers
│   ├── Cargo.toml
│   ├── ChangeLog
│   ├── LICENSE
│   ├── README.md
│   ├── doap.xml
│   ├── examples
│   │   └── generate-caps.rs
│   └── src
│       ├── attention.rs
│       ├── avatar.rs
│       ├── bind.rs
│       ├── blocking.rs
│       ├── bob.rs
│       ├── bookmarks.rs
│       ├── bookmarks2.rs
│       ├── caps.rs
│       ├── carbons.rs
│       ├── cert_management.rs
│       ├── chatstates.rs
│       ├── component.rs
│       ├── csi.rs
│       ├── data_forms.rs
│       ├── date.rs
│       ├── delay.rs
│       ├── disco.rs
│       ├── ecaps2.rs
│       ├── eme.rs
│       ├── extdisco.rs
│       ├── forwarding.rs
│       ├── hashes.rs
│       ├── http_upload.rs
│       ├── ibb.rs
│       ├── ibr.rs
│       ├── idle.rs
│       ├── iq.rs
│       ├── jid_prep.rs
│       ├── jingle.rs
│       ├── jingle_dtls_srtp.rs
│       ├── jingle_ft.rs
│       ├── jingle_grouping.rs
│       ├── jingle_ibb.rs
│       ├── jingle_ice_udp.rs
│       ├── jingle_message.rs
│       ├── jingle_raw_udp.rs
│       ├── jingle_rtcp_fb.rs
│       ├── jingle_rtp.rs
│       ├── jingle_rtp_hdrext.rs
│       ├── jingle_s5b.rs
│       ├── jingle_ssma.rs
│       ├── legacy_omemo.rs
│       ├── lib.rs
│       ├── mam.rs
│       ├── mam_prefs.rs
│       ├── media_element.rs
│       ├── message.rs
│       ├── message_correct.rs
│       ├── mix.rs
│       ├── mood.rs
│       ├── muc
│       │   ├── mod.rs
│       │   ├── muc.rs
│       │   └── user.rs
│       ├── nick.rs
│       ├── ns.rs
│       ├── occupant_id.rs
│       ├── openpgp.rs
│       ├── ping.rs
│       ├── presence.rs
│       ├── pubsub
│       │   ├── event.rs
│       │   ├── mod.rs
│       │   ├── owner.rs
│       │   └── pubsub.rs
│       ├── reactions.rs
│       ├── receipts.rs
│       ├── roster.rs
│       ├── rsm.rs
│       ├── rtt.rs
│       ├── sasl.rs
│       ├── server_info.rs
│       ├── sm.rs
│       ├── stanza_error.rs
│       ├── stanza_id.rs
│       ├── stream.rs
│       ├── time.rs
│       ├── tune.rs
│       ├── util
│       │   ├── error.rs
│       │   ├── helpers.rs
│       │   ├── macros.rs
│       │   └── mod.rs
│       ├── version.rs
│       ├── websocket.rs
│       └── xhtml.rs
├── tokio-xmpp
│   ├── Cargo.toml
│   ├── README.md
│   ├── build.rs
│   ├── examples
│   │   ├── contact_addr.rs
│   │   ├── download_avatars.rs
│   │   ├── echo_bot.rs
│   │   ├── echo_component.rs
│   │   └── send_message.rs
│   ├── logo.svg
│   └── src
│       ├── client
│       │   ├── async_client.rs
│       │   ├── auth.rs
│       │   ├── bind.rs
│       │   ├── mod.rs
│       │   └── simple_client.rs
│       ├── component
│       │   ├── auth.rs
│       │   └── mod.rs
│       ├── error.rs
│       ├── event.rs
│       ├── happy_eyeballs.rs
│       ├── lib.rs
│       ├── starttls.rs
│       ├── stream_features.rs
│       ├── stream_start.rs
│       ├── xmpp_codec.rs
│       └── xmpp_stream.rs
└── xmpp
    ├── Cargo.toml
    ├── ChangeLog
    ├── LICENSE
    ├── README.md
    ├── examples
    │   └── hello_bot.rs
    └── src
        ├── lib.rs
        └── pubsub
            ├── avatar.rs
            └── mod.rs

23 directories, 153 files
```

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules

<details closed><summary>Client</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                              | Module                                 |
|:-----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------|
| auth.rs          | This code provides an implementation of the Simple Authentication and Security Layer( SASL) protocol for authenticating a user with a server. It supports the mechanisms Anonymous, Plain, and Scram with SHA-1 and SHA-256 hashing algorithms. It uses the futures::stream::StreamExt, sasl::client::mechanisms     | tokio-xmpp/src/client/auth.rs          |
| mod.rs           | This code defines two modules, auth and bind, and two public modules, async_client and simple_client. The auth and bind modules provide authentication and binding functionality, while the async_client and simple_client modules provide asynchronous and simple client functionality.                             | tokio-xmpp/src/client/mod.rs           |
| simple_client.rs | This code implements a Client struct which provides a simple XMPP client connection. It implements the Stream and Sink traits from the futures crate, allowing for sending and receiving of XMPP packets. It provides methods for connecting to an XMPP server, sending stanzas, and ending the connection.          | tokio-xmpp/src/client/simple_client.rs |
| async_client.rs  | This code implements an XMPP client connection and state, allowing for the connection to be reconnected. It implements the ` futures ` crate's Stream and Sink traits, allowing for the sending and receiving of XMPP packets. It also provides methods for sending stanzas and ending the connection.               | tokio-xmpp/src/client/async_client.rs  |
| bind.rs          | This code provides a function to bind a resource to an XMPPStream, allowing the stream to be used for communication. It checks if the stream supports resource binding, and if so, sends a BindQuery and waits for a BindResponse. If the response is valid, the stream's JID is updated and the stream is returned. | tokio-xmpp/src/client/bind.rs          |

</details>

<details closed><summary>Component</summary>

| File    | Summary                                                                                                                                                                                                                                                                                                                                  | Module                           |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------|
| auth.rs | This code is an async function that authenticates a XMPPStream with a given password. It sends a handshake stanza with the given password and stream ID, and then loops until it receives either a handshake accept stanza or an error stanza. If the handshake accept stanza is received, the function returns Ok, otherwise it returns | tokio-xmpp/src/component/auth.rs |
| mod.rs  | This code creates a Component struct which simplifies the XMPPStream to a Stream / Sink of Elements( stanzas). It also provides methods to connect to an XMPP server, send stanzas, and end the connection.                                                                                                                              | tokio-xmpp/src/component/mod.rs  |

</details>

<details closed><summary>Examples</summary>

| File                | Summary                                                                                                                                                                                                                                                                                                               | Module                                  |
|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------|
| generate-caps.rs    | This code computes two kinds of caps( Caps and ECaps2) from a DiscoInfoResult, which is read from stdin. It then prints the results.                                                                                                                                                                                  | parsers/examples/generate-caps.rs       |
| articles.rs         | This code parses an XML document containing two articles and stores them in a vector of Article structs. It then prints out the vector of articles.                                                                                                                                                                   | minidom/examples/articles.rs            |
| hello_bot.rs        | This code is a bot written in Rust that uses the XMPP protocol. It connects to a server, joins rooms, sends messages, and retrieves avatars. It also handles events such as contacts being added, removed, or changed, as well as messages being sent or received.                                                    | xmpp/examples/hello_bot.rs              |
| echo_component.rs   | This code creates a Component instance and uses it to send and receive messages. It takes in four arguments: a JID, a password, a server, and a port. It then sends a presence message and enters a loop to process events. If a message is received, it will echo the message back.                                  | tokio-xmpp/examples/echo_component.rs   |
| send_message.rs     | This code is a program written in Rust that creates a simple XMPP client. It takes four arguments from the command line: a JID, a password, and a recipient. It then reads a message from standard input and sends it to the recipient. Finally, it closes the client connection.                                     | tokio-xmpp/examples/send_message.rs     |
| download_avatars.rs | This code is a main loop that processes events from an XMPP client. It handles incoming stanzas, such as IQs, messages, and presences, and responds accordingly. It also handles downloading avatars and saving them to a file.                                                                                       | tokio-xmpp/examples/download_avatars.rs |
| echo_bot.rs         | This code creates an XMPP client that connects to a server and echoes messages sent to it. It also has a secret command that triggers the client to disconnect from the server. It uses the futures::stream::StreamExt, std::convert::TryFrom, std::env::args, std::process::exit, tok                                | tokio-xmpp/examples/echo_bot.rs         |
| contact_addr.rs     | This code is a program that uses the Tokio XMPP library to connect to a server and query it for information about its admins, sales, security, support, feedback, and abuse contacts. It takes in four command line arguments, a JID, a password, and a target, and prints out the contact information for the server | tokio-xmpp/examples/contact_addr.rs     |

</details>

<details closed><summary>Icu</summary>

| File     | Summary                                                                                                                                                             | Module       |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------|
| build.rs | This code builds a C file called " bindings.c " and compiles it into a library called " bindings ". It also links two dynamic libraries, " icuuc " and " icui18n ". | icu/build.rs |

</details>

<details closed><summary>Muc</summary>

| File    | Summary                                                                                                                                                                                                                                                                                              | Module                  |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------|
| user.rs | Error fetching summary.                                                                                                                                                                                                                                                                              | parsers/src/muc/user.rs |
| muc.rs  | This code provides functions to create and manipulate elements for joining a Multi- User Chat( MUC) room, as well as elements for requesting history from the room. It includes functions to set the password, maximum characters, maximum stanzas, seconds, and since date for the history request. | parsers/src/muc/muc.rs  |
| mod.rs  | This code provides two modules, ` muc ` and ` user `, which implement the ` http://jabber.org/protocol/muc ` and ` http://jabber.org/protocol/muc#user ` protocols respectively. It also provides two public functions, ` Muc ` and ` MucUser `,                                                     | parsers/src/muc/mod.rs  |

</details>

<details closed><summary>Parsers</summary>

| File      | Summary                 | Module            |
|:----------|:------------------------|:------------------|
| ChangeLog | Error fetching summary. | parsers/ChangeLog |
| doap.xml  | Error fetching summary. | parsers/doap.xml  |

</details>

<details closed><summary>Pubsub</summary>

| File      | Summary                                                                                                                                                                                                                                                                   | Module                       |
|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------|
| owner.rs  | This code provides a set of elements used to communicate with a PubSubOwner service, such as Affiliations, Configure, Default, Delete, Purge, and Subscriptions. It also provides a PubSubOwner enum to represent the payloads used to communicate with the service.      | parsers/src/pubsub/owner.rs  |
| event.rs  | Error fetching summary.                                                                                                                                                                                                                                                   | parsers/src/pubsub/event.rs  |
| mod.rs    | This code provides a set of modules for the ` http://jabber.org/protocol/pubsub ` protocol, as well as associated types and functions. It allows for the creation of PubSub nodes, items, and subscriptions, and provides a way to convert between elements and payloads. | parsers/src/pubsub/mod.rs    |
| pubsub.rs | Error fetching summary.                                                                                                                                                                                                                                                   | parsers/src/pubsub/pubsub.rs |
| avatar.rs | This code handles the retrieval of avatar data from a PubSub event. It checks the metadata of the avatar, and if the file is not present, it sends an IQ to download the data. It then saves the data to a file and returns an event to the caller.                       | xmpp/src/pubsub/avatar.rs    |
| mod.rs    | This code handles events and IQ results related to PubSub nodes, such as bookmarks2 and avatars. It processes the events and results to generate JoinRoom, LeaveRoom, and LeaveAllRooms events.                                                                           | xmpp/src/pubsub/mod.rs       |

</details>

<details closed><summary>Src</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                                                                               | Module                            |
|:---------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------|
| message.rs           | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/message.rs            |
| stanza_id.rs         | This code defines two structs, StanzaId and OriginId, which are used to track messages in a MUC. StanzaId is used to identify a stanza by another entity, and OriginId is used to track a message which may have its' i d' attribute changed. Both structs implement the MessagePayload trait.                                                                        | parsers/src/stanza_id.rs          |
| mood.rs              | This code creates an enum representing all of the possible values of the XEP-0107 moods, as well as a free- form text description of the mood. It also provides a test suite to ensure the code is working correctly.                                                                                                                                                 | parsers/src/mood.rs               |
| ns.rs                | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/ns.rs                 |
| carbons.rs           | This code provides implementations of the XMPP Carbons protocol, which allows for the synchronization of messages between multiple resources of a user. It includes implementations of the Enable, Disable, Private, Received, and Sent elements, which are used to enable / disable carbons, request that a message not be copied, and wrap messages received / sent | parsers/src/carbons.rs            |
| jingle_grouping.rs   | This code defines the structs ` Semantics `, ` Content `, and ` Group ` which are used to describe a semantic group of contents. The ` Group ` struct contains a ` Semantics ` attribute and a list of ` Content ` elements. The ` Content ` element contains a ` name ` attribute which is used to match a ` Content                                                 | parsers/src/jingle_grouping.rs    |
| server_info.rs       | This code provides a structure representing a ` http://jabber.org/network/serverinfo ` form type, which contains fields for abuse, admin, feedback, sales, security, and support addresses. It also provides functions to convert between the structure and a DataForm.                                                                                               | parsers/src/server_info.rs        |
| stream.rs            | This code creates a Stream element for client- server communications. It includes attributes such as from, to, i d, version, and xml_lang. It also provides methods to set these attributes and to check if the version matches the expected one.                                                                                                                     | parsers/src/stream.rs             |
| avatar.rs            | This code provides implementations of the Metadata, Info, and Data elements for the XMPP Avatar protocol. It allows for the communication of information about an avatar, such as its size, SHA-1 hash, content type, and URL. It also provides a vector of bytes representing the avatar's image.                                                                    | parsers/src/avatar.rs             |
| sm.rs                | This code provides definitions for the Stream Management XMPP extension, which allows for the acknowledgement of received stanzas and the resumption of a previous stream. It includes definitions for elements such as < a >, < enable >, < enabled >, < failed >, < r >, < resume >, and < resumed >, as well as attributes such                                    | parsers/src/sm.rs                 |
| jingle_raw_udp.rs    | This code provides a wrapper element for an raw UDP transport, as well as a candidate element for an ICE- UDP session. It allows for the creation of a new transport, and the addition of a candidate to the transport. It also provides attributes for the candidate such as component, generation, i d, ip, port, and type.                                         | parsers/src/jingle_raw_udp.rs     |
| presence.rs          | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/presence.rs           |
| jingle_ft.rs         | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/jingle_ft.rs          |
| forwarding.rs        | This code defines a Forwarded element which contains a forwarded stanza, either standalone or part of another extension( such as carbons). It contains two optional children, a Delay element and a Message element. It is used to serialize and deserialize the Forwarded element.                                                                                   | parsers/src/forwarding.rs         |
| reactions.rs         | This code defines two structs, Reactions and Reaction, which are used to store a set of emoji reactions to a message. The Reactions struct contains an i d field, which is the i d of the message the reactions apply to, and a reactions field, which is a vector of Reaction structs. The Reaction struct contains a single field                                   | parsers/src/reactions.rs          |
| stanza_error.rs      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/stanza_error.rs       |
| jingle_ibb.rs        | This code creates a Transport element for In- Band Bytestreams( XEP-0047) in Jingle. It requires a block size and stream identifier, and has an optional stanza type attribute.                                                                                                                                                                                       | parsers/src/jingle_ibb.rs         |
| ibb.rs               | This code provides functions to generate elements for In- Band Bytestreams( IBB) in the Extensible Messaging and Presence Protocol( XMPP). It includes functions to open a stream, exchange data, and close a stream. It also includes functions to generate identifiers and attributes for the elements.                                                             | parsers/src/ibb.rs                |
| eme.rs               | This code defines a structure representing an ` < encryption xmlns='urn: xmpp: eme:0'/ > ` element, which is used to encrypt messages. It implements the MessagePayload trait and contains two attributes: namespace( required) and name( optional). It also provides a test suite and a serialisation method.                                                        | parsers/src/eme.rs                |
| http_upload.rs       | This code is a part of the XMPP protocol which allows for the transfer of files over the internet. It includes functions for requesting a slot, creating a slot result, and creating elements for a put and get URL.                                                                                                                                                  | parsers/src/http_upload.rs        |
| csi.rs               | This code defines three empty elements( Feature, Inactive, and Active) for the Client State Indication( CSI) protocol. It also includes tests to ensure the elements are correctly parsed and serialized.                                                                                                                                                             | parsers/src/csi.rs                |
| disco.rs             | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/disco.rs              |
| jingle_rtcp_fb.rs    | This code creates a Rust macro to generate a wrapper element for a rtcp- fb. It also includes a test module to ensure the size of the element is correct and to test the parsing of a simple rtcp- fb element.                                                                                                                                                        | parsers/src/jingle_rtcp_fb.rs     |
| version.rs           | This code provides a set of functions to generate and parse an < iq > element for a version query and result. It allows for the retrieval of the name, version, and operating system of a remote entity.                                                                                                                                                              | parsers/src/version.rs            |
| receipts.rs          | This code defines two structs, Request and Received, which are used to implement the XMPP Receipts protocol. Request is used to request an acknowledgement from the recipient of a message, and Received is used to acknowledge a previously received message. The code also includes tests for the structs.                                                          | parsers/src/receipts.rs           |
| mam_prefs.rs         | This code provides a Rust implementation of the XMPP Message Archive Management( MAM) Prefs element, which controls the archiving preferences of the user. It implements the IqGetPayload, IqSetPayload, and IqResultPayload traits, allowing it to be used in XMPP IQ requests and responses                                                                         | parsers/src/mam_prefs.rs          |
| extdisco.rs          | This code defines structures for representing service elements and their associated attributes, as well as functions for converting them to and from XMPP elements. It also defines structures for representing service queries and results, and functions for converting them to and from XMPP elements.                                                             | parsers/src/extdisco.rs           |
| lib.rs               | XEP-0452: Software Information                                                                                                                                                                                                                                                                                                                                        | parsers/src/lib.rs                |
|                      |  pub mod software_info;                                                                                                                                                                                                                                                                                                                                               |                                   |
|                      |                                                                                                                                                                                                                                                                                                                                                                       |                                   |
|                      |  /// XEP-0455: Message Processing Hints                                                                                                                                                                                                                                                                                                                               |                                   |
|                      |  pub mod hints;                                                                                                                                                                                                                                                                                                                                                       |                                   |
|                      |                                                                                                                                                                                                                                                                                                                                                                       |                                   |
|                      |  /// XEP-0466: Data Forms Media Element                                                                                                                                                                                                                                                                                                                               |                                   |
|                      |  pub mod data_forms_media_element;                                                                                                                                                                                                                                                                                                                                    |                                   |
|                      |                                                                                                                                                                                                                                                                                                                                                                       |                                   |
|                      |  /// XEP-0480: OM                                                                                                                                                                                                                                                                                                                                                     |                                   |
| time.rs              | This code provides a TimeQuery and TimeResult structs which allow for the parsing of an XMPP time query and result. It also provides implementations of IqGetPayload and IqResultPayload for the TimeQuery and TimeResult structs, respectively.                                                                                                                      | parsers/src/time.rs               |
| idle.rs              | This code defines the Idle struct, which is used to represent the last time a user interacted with their system. It implements the PresencePayload trait and has one required attribute,' since', which is a DateTime representing the time at which the user stopped interacting.                                                                                    | parsers/src/idle.rs               |
| message_correct.rs   | This code defines a Replace struct which implements the MessagePayload trait. It is used to replace a previous message, identified by the' i d' attribute. It also contains tests to ensure the validity of the code.                                                                                                                                                 | parsers/src/message_correct.rs    |
| xhtml.rs             | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/xhtml.rs              |
| legacy_omemo.rs      | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/legacy_omemo.rs       |
| jingle_dtls_srtp.rs  | This code provides a Fingerprint struct which is used to store the hash algorithm, setup, and hash value of a DTLS handshake. It also provides a method to create a Fingerprint from a Setup and a Hash.                                                                                                                                                              | parsers/src/jingle_dtls_srtp.rs   |
| attention.rs         | This code defines an Attention struct which implements the MessagePayload trait. It is used to request the attention of the recipient. It has no attributes or children and is defined by the urn: xmpp: attention:0 namespace.                                                                                                                                       | parsers/src/attention.rs          |
| jingle_ssma.rs       | This code provides functions to generate elements for the ssrc SDP attribute, including Source, Parameter, Semantics, and Group elements. It also provides a function to create a new SSMA Source element.                                                                                                                                                            | parsers/src/jingle_ssma.rs        |
| ecaps2.rs            | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/ecaps2.rs             |
| roster.rs            | This code defines structs and methods for representing a user's contact list, including contact information and subscription status. It also provides methods for converting between the structs and XML elements.                                                                                                                                                    | parsers/src/roster.rs             |
| hashes.rs            | This code provides functions for parsing and serializing a hash element, which is used to represent a hash of some data, defined by the hash algorithm used and the computed value. It supports the Secure Hash Algorithm 1, 2, and 3, as well as the BLAKE2 hash algorithm. It also provides functions for converting the hash                                       | parsers/src/hashes.rs             |
| openpgp.rs           | This code provides functions to generate elements for the PubKey, PubKeyData, PubKeyMeta, and PubKeysMeta structs, as well as implementations of the PubSubPayload trait for the PubKey and PubKeysMeta structs. It also provides tests to ensure the serialization of the PubKey element is correct.                                                                 | parsers/src/openpgp.rs            |
| chatstates.rs        | This code creates an enum representing chatstate elements part of the ` http://jabber.org/protocol/chatstates ` namespace, and implements the MessagePayload trait for it. It also provides tests to ensure the validity of the code.                                                                                                                                 | parsers/src/chatstates.rs         |
| date.rs              | This code implements the DateTime profile of XEP-0082, which represents a non- recurring moment in time, with an accuracy of seconds or fraction of seconds, and includes a timezone. It provides methods to retrieve the associated timezone, create a new DateTime with a different timezone, and format the DateTime with                                          | parsers/src/date.rs               |
| nick.rs              | This code creates a Nick element, which represents a global, memorable, friendly or informal name chosen by a user. It is used to generate an element ID, and includes tests to ensure the size and validity of the element. It is covered by the Mozilla Public License, v. 2.0.                                                                                     | parsers/src/nick.rs               |
| bookmarks2.rs        | This code provides a struct and associated functions to represent a conference bookmark in the XMPP protocol. It includes functions to convert between the struct and an XML element, as well as functions to set and get attributes such as autojoin, name, nick, and password.                                                                                      | parsers/src/bookmarks2.rs         |
| websocket.rs         | This code creates an Open element for WebSocket stream opening, which contains attributes such as from, to, i d, version, and xml_lang. It also provides methods to set these attributes and to check if the version matches the expected one.                                                                                                                        | parsers/src/websocket.rs          |
| ping.rs              | This code creates a Ping struct which implements the IqGetPayload trait. It is used to represent a ping to the recipient, which must be answered with an empty < iq/ > or with an error. It is subject to the terms of the Mozilla Public License, v. 2.0.                                                                                                            | parsers/src/ping.rs               |
| caps.rs              | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/caps.rs               |
| rtt.rs               | This code provides support for real- time text transmission, including key presses, text block inserts, backspace key presses, delete key presses, and text block deletes. It also allows for the transmission of intervals, between real- time text actions, to recreate the pauses between key presses.                                                             | parsers/src/rtt.rs                |
| bob.rs               | This code defines a ContentId struct, which is used to represent a Content- ID as defined in RFC2111. It also defines a Data struct, which is used to request an uncached cid file. Both structs implement the FromStr and IntoAttributeValue traits. Additionally, the size of the structs is tested.                                                                | parsers/src/bob.rs                |
| bookmarks.rs         | This code defines structs and methods for creating and manipulating bookmarks in an XMPP client. It includes structs for Conference and Url bookmarks, as well as a Storage struct for containing multiple bookmarks. It also provides methods for creating an empty Storage and for converting between Element and Storage.                                          | parsers/src/bookmarks.rs          |
| mix.rs               | This code provides a set of Rust structs and functions to interact with the XMPP MIX protocol. It includes structs for Participant, Subscribe, Join, UpdateSubscription, Leave, SetNick, Mix, Create, and Destroy elements, as well as functions to create and serialize them. It also includes ParticipantId and Channel                                             | parsers/src/mix.rs                |
| jingle_rtp_hdrext.rs | This code defines a struct called RtpHdrext which contains attributes for an ID, URI, and Senders. It also provides a constructor for creating a new RtpHdrext element and a method for setting the senders. Additionally, it includes a test to check the size of the struct.                                                                                        | parsers/src/jingle_rtp_hdrext.rs  |
| ibr.rs               | This code is a Rust implementation of the XMPP In- Band Registration( IBR) protocol, which allows users to register for a service using an XMPP client. It provides functions for creating and parsing IBR queries, which contain instructions, fields, and data forms for the user to fill out. It also supports the ability                                         | parsers/src/ibr.rs                |
| component.rs         | This code provides a Handshake struct which is used as the main authentication mechanism for components. It contains a data field which is either None, or contains the hex- encoded SHA-1 of the concatenation of the stream i d and the password. The code also provides two constructors, one to create a successful reply from a server                           | parsers/src/component.rs          |
| rsm.rs               | This code provides functions to request paging through a potentially big set of items( represented by an UID) and to describe the paging result of a query.                                                                                                                                                                                                           | parsers/src/rsm.rs                |
| jingle_rtp.rs        | This code defines a Description struct which is a wrapper element describing an RTP session. It contains attributes such as media, ssrc, and children such as payload_types, rtcp_mux, ssrc_groups, ssrcs, and hdrexts. It also contains functions to create a new RTP                                                                                                | parsers/src/jingle_rtp.rs         |
| jingle_ice_udp.rs    | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/jingle_ice_udp.rs     |
| mam.rs               | This code provides a set of structs and functions for creating and parsing XMPP elements related to Message Archive Management( MAM). It includes structs for creating and parsing Query, Result _, Complete, and Fin elements, as well as functions for creating and parsing IqGetPayload, IqSetPayload, I                                                           | parsers/src/mam.rs                |
| jingle_s5b.rs        | This code provides a Jingle transport using a direct or proxied connection. It includes attributes for the stream identifier, destination address, mode, and payload. It also includes functions for creating a new transport, setting the destination address, mode, and payload.                                                                                    | parsers/src/jingle_s5b.rs         |
| delay.rs             | This code defines a Delay struct which stores information about when and by whom a message was stored for later delivery. It includes attributes for the entity which delayed the message and the time at which it was stored, as well as an optional reason for the delay. It also implements the MessagePayload and PresencePayload traits.                         | parsers/src/delay.rs              |
| tune.rs              | This code provides functions to generate elements for the Tune namespace, which is used to provide information about a song or piece. It also provides a TryFrom implementation for the Tune struct, which contains fields for the artist, length, rating, source, title, track, and uri of the song or piece.                                                        | parsers/src/tune.rs               |
| occupant_id.rs       | This code defines the OccupantId struct, which is used to uniquely identify a MUC participant across reconnects and renames. It implements the MessagePayload and PresencePayload traits, and contains an " i d " attribute which is required. It also contains tests to ensure the struct is functioning correctly.                                                  | parsers/src/occupant_id.rs        |
| jingle.rs            | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/jingle.rs             |
| cert_management.rs   | This code provides a set of functions to manage X.509 certificates for SASL authentication. It includes functions to append, disable, and revoke certificates, as well as to list the current certificates.                                                                                                                                                           | parsers/src/cert_management.rs    |
| bind.rs              | This code provides functions for resource binding, which is the process by which a client can obtain a full JID and start exchanging on the XMPP network. It includes functions for creating a resource binding request, as well as for parsing a response containing the client's full JID.                                                                          | parsers/src/bind.rs               |
| jid_prep.rs          | This code provides two elements, JidPrepQuery and JidPrepResponse, which are used to request and respond to a stringprep / PRECIS operation on a string to turn it into a JID.                                                                                                                                                                                        | parsers/src/jid_prep.rs           |
| sasl.rs              | This code provides functions to generate elements and attributes for the SASL protocol. It also provides a Failure struct to represent a failure element sent by the server.                                                                                                                                                                                          | parsers/src/sasl.rs               |
| jingle_message.rs    | This code defines a protocol for broadcasting Jingle requests to all of the clients of a user. It includes functions for proposing, retracting, accepting, proceeding, and rejecting a session.                                                                                                                                                                       | parsers/src/jingle_message.rs     |
| iq.rs                | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | parsers/src/iq.rs                 |
| lib.rs               | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | jid/src/lib.rs                    |
| tree_builder.rs      | This code creates a TreeBuilder struct which is used to convert SAX events to DOM tree. It contains methods to create a new TreeBuilder, set prefixes stack, get stack depth, get top- most element from the stack, pop the top- most element from the stack, unshift the first child of the top element, lookup                                                      | minidom/src/tree_builder.rs       |
| element.rs           | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | minidom/src/element.rs            |
| convert.rs           | This module provides traits for converting types to elements and attributes. It includes implementations for various types such as usize, u64, u32, u16, u8, isize, i64, i32, i16, i8, and std::net::IpAddr. It also includes implementations for String, &                                                                                                           | minidom/src/convert.rs            |
| error.rs             | This code provides an error type for a crate, with the ability to convert from rxml errors. It also provides a simplified Result type for the crate.                                                                                                                                                                                                                  | minidom/src/error.rs              |
| lib.rs               | pub use prefixes::Prefixes;                                                                                                                                                                                                                                                                                                                                           | minidom/src/lib.rs                |
|                      |  pub use tree_builder::TreeBuilder;                                                                                                                                                                                                                                                                                                                                   |                                   |
|                      |                                                                                                                                                                                                                                                                                                                                                                       |                                   |
|                      |  /// Parse an XML string into an ` Element `.                                                                                                                                                                                                                                                                                                                         |                                   |
|                      |  ///                                                                                                                                                                                                                                                                                                                                                                  |                                   |
|                      |  /// # Example                                                                                                                                                                                                                                                                                                                                                        |                                   |
|                      |  ///                                                                                                                                                                                                                                                                                                                                                                  |                                   |
|                      |  /// ` ` `                                                                                                                                                                                                                                                                                                                                                            |                                   |
|                      |  /// use minidom::parse;                                                                                                                                                                                                                                                                                                                                              |                                   |
|                      |  ///                                                                                                                                                                                                                                                                                                                                                                  |                                   |
|                      |  /// let root = parse("<root><child/></root                                                                                                                                                                                                                                                                                                                           |                                   |
| namespaces.rs        | This code provides an enum, NSChoice, which is used to compare namespaces. It also provides an implementation of From for NSChoice, which allows a & str to be converted into an NSChoice. Finally, it provides a compare method which takes a & str and returns a boolean based on the comparison of the & str to the NS                                             | minidom/src/namespaces.rs         |
| node.rs              | This code provides the ` Node ` struct, which represents a node in the DOM. It can be an ` Element ` or a text node, and provides methods to convert between the two. It also provides methods to write the node to an ` ItemWriter `.                                                                                                                                | minidom/src/node.rs               |
| prefixes.rs          | This code creates a Prefixes struct which stores a BTreeMap of Prefix and Namespace values. It also provides methods to insert, get, and declare prefixes. It implements the From trait to allow for conversion from various types.                                                                                                                                   | minidom/src/prefixes.rs           |
| lib.rs               | Error fetching summary.                                                                                                                                                                                                                                                                                                                                               | xmpp/src/lib.rs                   |
| xmpp_stream.rs       | XMPPStream provides encoding / decoding for XMPP packets, wrapping a binary stream( tokio's ` AsyncRead + AsyncWrite `) to decode and encode XMPP packets. It implements ` Sink + Stream ` and provides methods to send and receive XMPP packets.                                                                                                                     | tokio-xmpp/src/xmpp_stream.rs     |
| xmpp_codec.rs        | This is an XML stream parser for XMPP, which provides a stateful encoder / decoder for a bytestream from / to XMPP ` Packet`s. It supports encoding and decoding of ` < stream: stream > ` start tags, complete stanzas or nonzas, plain text, and `                                                                                                                  | tokio-xmpp/src/xmpp_codec.rs      |
| happy_eyeballs.rs    | This code provides a function to connect to a host using a domain name or IP address. It first attempts to connect using the domain name, and if that fails, it will attempt to connect using the IP address. If the domain name is not an IP address, it will also attempt to connect using a SRV record. If all attempts                                            | tokio-xmpp/src/happy_eyeballs.rs  |
| stream_start.rs      | This code creates an XMPPStream from a Framed stream, sending a < stream: stream > element and waiting for one from the server. It then parses the stream attributes and features, and returns an XMPPStream.                                                                                                                                                         | tokio-xmpp/src/stream_start.rs    |
| error.rs             | This code defines an enum Error which is a top- level error type for XMPP protocol- level errors. It includes errors for I / O, DNS resolution, XML parsing, authentication, TLS, and more. It also includes a ParseError type for XML parse errors and a ConnecterError type for errors establishing a connection.                                                   | tokio-xmpp/src/error.rs           |
| stream_features.rs   | This code contains a wrapper for the ` < stream: features/ > ` nonza, which is usually the first nonza of an XMPPStream. It provides methods to check if the server can initiate a TLS session, iterate over SASL mechanisms, and check if the server supports user resource binding.                                                                                 | tokio-xmpp/src/stream_features.rs |
| lib.rs               | This code is an implementation of the XMPP protocol using asynchronous I / O with Tokio. It provides features such as authentication, connection, and parsing of packets. It also provides a Component API for creating XMPP components. Additionally, it provides an error module for handling errors related to the XMPP protocol.                                  | tokio-xmpp/src/lib.rs             |
| starttls.rs          | This code provides a function to perform the StartTLS protocol on an XMPPStream, which is used to establish a secure connection. It uses the futures crate to stream and sink data, and the tokio crate to handle asynchronous I / O. Depending on the feature flag, it uses either the native- tls or rust                                                           | tokio-xmpp/src/starttls.rs        |
| event.rs             | This code defines the Event enum which is used by Client and Component to represent high- level events on the Stream. It provides methods to check if the event is Online, get the server- assigned JID, check if the event is a Stanza, get the Stanza data, and unwrap the Stanza data.                                                                             | tokio-xmpp/src/event.rs           |
| bindings.c           | This code is a wrapper to avoid the automated suffixing libicu does in unicode / urename.h. It provides functions to convert between ASCII and Unicode, open and prepare a string, set the trace level, open a spoof checker, and set spoof checks.                                                                                                                   | icu/src/bindings.c                |
| error.rs             | This code provides a library for wrapping what is needed from ICU's C API for JIDs. It includes an enum for errors that can be produced by the library, as well as implementations of From for UErrorCode, std::string::FromUtf8Error, and std::char::DecodeUtf16Error. It                                                                                            | icu/src/error.rs                  |
| lib.rs               | This code provides a struct, Icu, which exposes the needed ICU functions to JID. It includes functions for stringprep profiles( Nameprep, Nodeprep, Resourceprep, and Saslprep), IDNA2008 support, and a spoof checker. It also provides an enum, Strict, to specify how un                                                                                           | icu/src/lib.rs                    |
| spoof.rs             | This code provides a wrapper for the ICU C API for JIDs, allowing users to transform a string into a skeleton for matching it with other potentially similar strings.                                                                                                                                                                                                 | icu/src/spoof.rs                  |
| stringprep.rs        | This code provides a struct for wrapping the ICU C API for JIDs. It allows for the conversion of a given string to UTF-16, the performance of a stringprep operation, and the conversion back to UTF-8. It also provides a flag for allowing unassigned characters.                                                                                                   | icu/src/stringprep.rs             |
| bindings.rs          | This code provides a crate wrapping what is needed from ICU's C API for JIDs. It includes functions from unicode / ustring.h, unicode / usprep.h, unicode / utrace.h, unicode / uidna.h, and unicode / uspoof.h. These functions allow                                                                                                                                | icu/src/bindings.rs               |
| idna2008.rs          | This code provides a struct, Idna, which wraps the ICU C API for JIDs. It provides functions to convert a domain name into its ASCII or Unicode form for DNS lookup or human- readable display. It also checks for errors and ensures that the domain name is not too long.                                                                                           | icu/src/idna2008.rs               |

</details>

<details closed><summary>Tokio-xmpp</summary>

| File     | Summary                                                                                                                                                                                                              | Module              |
|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|
| build.rs | This code creates a loop that prints out a string for each major and minor version of the Rust compiler, up to the current version. It uses the rustc_version crate to get the current version of the Rust compiler. | tokio-xmpp/build.rs |
| logo.svg | Error fetching summary.                                                                                                                                                                                              | tokio-xmpp/logo.svg |

</details>

<details closed><summary>Util</summary>

| File       | Summary                                                                                                                                                                                                             | Module                      |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| error.rs   | This code defines the Error enum which contains potential errors triggered while parsing an Element into a specialised struct. It also implements the StdError trait and the fmt::Display trait for the Error enum. | parsers/src/util/error.rs   |
| helpers.rs | This code provides a set of codecs for encoding and decoding various types of data, such as text, plain text, trimmed plain text, base64, whitespace- aware base64, colon- separated hexadecimal, and JID.          | parsers/src/util/helpers.rs |
| mod.rs     | This code provides an error type and various helpers and macros to parse and serialise data more easily. It is copyright( c) 2019 Emmanuel Gil Peyrot and is subject to the Mozilla Public License, v. 2.0.         | parsers/src/util/mod.rs     |
| macros.rs  | Error fetching summary.                                                                                                                                                                                             | parsers/src/util/macros.rs  |

</details>

<details closed><summary>Xmpp</summary>

| File      | Summary                                                                                                                                                                                                                                                                                                                            | Module         |
|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
| ChangeLog | Version 0.4.0 of xmpp- rs is a major update that includes breaking changes, improvements, and changes. Breaking changes include Event::ChatMessage and Event::RoomMessage now including an optional message i d. Improvements include the addition of a new Event::ServiceMessage, Event::HttpUploadedFile, a disconnect method on | xmpp/ChangeLog |

</details>

<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the xmpp-rs repository:
```sh
git clone https://gitlab.com/xmpp-rs/xmpp-rs
```

2. Change to the project directory:
```sh
cd xmpp-rs
```

3. Install the dependencies:
```sh
cargo build
```

### 🤖 Using xmpp-rs

```sh
cargo run
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />


## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---

