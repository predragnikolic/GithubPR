# Setup Language Server

Follow the setup steps for a language server to get it up and running.

If you encounter problems, see the [common issues](/setup/common_issues/) page or search the [LSP/issues](https://github.com/sublimelsp/LSP/issues) before opening new ones.

If there are no setup steps for a language server on this page, but a [language server implementation](https://microsoft.github.io/language-server-protocol/implementors/servers/) exist, follow the guide for [creating a client configuration](/setup/client_configuration/).

!!! tip
    We recommend installing [LSP-json](https://packagecontrol.io/packages/LSP-json), as it suggest smart settings completions and report errors when inside the `LSP.sublime-settings` file.




## Angular

Follow installation instructions on [LSP-angular](https://github.com/sublimelsp/LSP-angular).

## Bash

Follow installation instructions on [LSP-bash](https://github.com/sublimelsp/LSP-bash).

## C/C++

TODO add setup steps

## C\#

Follow installation instructions on [LSP-OmniSharp](https://github.com/sublimelsp/LSP-OmniSharp). (not available on Package Control)

## CMake

Follow installation instructions on [LSP-cmake](https://github.com/sublimelsp/LSP-cmake). (not available on Package Control)

## Clojure

1. Download [clojure-lsp](https://github.com/snoe/clojure-lsp).
2. Add the `"clojure-lsp"` configuration to the `LSP.sublime-settings` file:

```json
{
    "clients": {
        "clojure-lsp": {
            "enabled": true,
            "command": ["java", "-jar", "/PATH/TO/clojure-lsp"],
            "initializationOptions": {}, // see all available options https://github.com/snoe/clojure-lsp#initializationoptions
            "selector": "source.clojure"
        }
    }
}
```
3. Update the `/PATH/TO/clojure-lsp`.

## CSS

Follow installation instructions on [LSP-css](https://github.com/sublimelsp/LSP-css).

## D

TODO add setup steps

## Dart

Follow installation instructions on [LSP-Dart](https://github.com/sublimelsp/LSP-Dart).

## Dockerfile

Follow installation instructions on [LSP-dockerfile](https://github.com/sublimelsp/LSP-dockerfile).

## Elixir

Follow installation instructions on [LSP-elixir](https://github.com/sublimelsp/LSP-elixir).

## Elm

Follow installation instructions on [LSP-elm](https://github.com/sublimelsp/LSP-elm).

## Erlang

TODO add setup steps

## ESLint

Follow installation instructions on [LSP-eslint](https://github.com/sublimelsp/LSP-eslint).

## Flow

Follow installation instructions on [LSP-flow](https://github.com/sublimelsp/LSP-flow). (not available on Package Control)

## Fortran

TODO add setup steps

## GO

TODO add setup steps

## GraphQL

Follow installation instructions on [LSP-graphql](https://github.com/sublimelsp/LSP-graphql).

## Haskell

TODO add setup steps

## HTML

Follow installation instructions on [LSP-html](https://github.com/sublimelsp/LSP-html).

## Java

Follow installation instructions on [LSP-jdtls](https://github.com/sublimelsp/LSP-jdtls). (not available on Package Control)

## JSON

Follow installation instructions on [LSP-json](https://github.com/sublimelsp/LSP-json).

## Julia

Follow installation instructions on [LSP-julia](https://github.com/sublimelsp/LSP-julia). (not available on Package Control)

## Kotlin

TODO add setup steps

## LaTeX

Follow installation instructions on [LSP-TexLab](https://github.com/sublimelsp/LSP-TexLab).

## Lisp

1. Install [cc-lsp](https://github.com/cxxxr/cl-lsp) using Roswell.
2. Add the `"cc-lsp"` configuration to the `LSP.sublime-settings` file:

```json
{
    "clients": {
        "cc-lsp": {
            "enabled": true,
            "command": ["cl-lsp", "stdio"],
            "selector": "source.lisp"
        }
    }
}
```

## Lua

Follow installation instructions on [LSP-lua](https://github.com/sublimelsp/LSP-lua). (not available on Package Control)

## OCaml/Reason

TODO add setup steps

## PromQL

Follow installation instructions on [LSP-promql](https://github.com/prometheus-community/sublimelsp-promql).

## PHP

Multiple options:

* Follow installation instructions on [LSP-intelephense](https://github.com/sublimelsp/LSP-intelephense).
* Follow installation instructions on [LSP-serenata](https://github.com/Cloudstek/LSP-serenata).

## Polymer

TODO add setup steps

## PowerShell

Follow installation instructions on [LSP-PowerShellEditorServices](https://github.com/sublimelsp/LSP-PowerShellEditorServices). (not available on Package Control)

## Python

Multiple options:

* Follow installation instructions on [LSP-pyls](https://github.com/sublimelsp/LSP-pyls).
* Follow installation instructions on [LSP-pyright](https://github.com/sublimelsp/LSP-pyright).
* Follow installation instructions on [LSP-anakin](https://github.com/sublimelsp/LSP-anakin). (not available on Package Control)

## R

TODO add setup steps

## Ruby/Ruby on Rails

TODO add setup steps

## Rust

TODO add setup steps

## Scala

Follow installation instructions on [LSP-metals](https://github.com/scalameta/metals-sublime).

## SonarLint

Follow installation instructions on [LSP-SonarLint](https://github.com/sublimelsp/LSP-SonarLint). (not available on Package Control)

## SourceKit

Follow installation instructions on [LSP-SourceKit](https://github.com/sublimelsp/LSP-SourceKit). (not available on Package Control)

## Stylelint

Follow installation instructions on [LSP-stylelint](https://github.com/sublimelsp/LSP-stylelint).

## Svelte

Follow installation instructions on [LSP-svelte](https://github.com/sublimelsp/LSP-svelte).

## Swift

TODO add setup steps

## TAGML

Follow installation instructions on [LSP-tagml](https://github.com/HuygensING/LSP-tagml).

## Terraform

TODO add setup steps

## TypeScript / JavaScript

Follow installation instructions on [LSP-typescript](https://github.com/HuygensING/LSP-typescript).

## Vue

Follow installation instructions on [LSP-vue](https://github.com/sublimelsp/LSP-vue).

## XML

Follow installation instructions on [LSP-lemminx](https://github.com/sublimelsp/LSP-lemminx).

## YAML

Follow installation instructions on [LSP-yaml](https://github.com/sublimelsp/LSP-yaml).
