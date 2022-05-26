loader = yaml.SafeLoader
loader.add_constructor(
    "!ReplaceWithConfig", partial(replace_with_config_constructor, config=config)
)
