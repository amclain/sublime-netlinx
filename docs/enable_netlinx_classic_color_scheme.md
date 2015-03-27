Enable NetLinx Classic Color Scheme
===================================
Open a NetLinx **.axs** or **.axi** source code file in Sublime Text.

On the menu bar, go to Preferences -> Settings - More -> Syntax-Specific - User

Insert the following code and save the file:

``` json
{
    "color_scheme": "Packages/NetLinx/NetLinx.tmTheme"
}
```

The NetLinx classic color scheme will now be automatically applied to all .axs
and .axi files that are opened in Sublime Text. Other file types will not be
affected.
