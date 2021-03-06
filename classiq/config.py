"""Configuration of the SDK module."""
import os
import pathlib
from typing import List, Union, Optional

import configargparse
import pydantic


class WebsocketURI(pydantic.AnyUrl):
    allowed_schemes = {"ws", "wss"}


class Configuration(pydantic.BaseModel):
    """Object containing configuration options (see description in fields)."""

    host: pydantic.AnyHttpUrl = pydantic.Field(..., description="Classiq backend URI.")
    ws_uri: WebsocketURI = pydantic.Field(
        default=None,
        description="Web socket URI, derived automatically from the host field.",
    )

    @pydantic.validator("ws_uri", always=True)
    def validate_ws_uri(cls, v, values) -> WebsocketURI:
        if v is not None:
            return v

        host = values.get("host")
        if host is None:
            raise ValueError("Can not init ws_uri with out a valid host")

        scheme = "wss" if host.scheme == "https" else "ws"
        port = f":{host.port}" if host.port else ""
        return pydantic.parse_obj_as(WebsocketURI, f"{scheme}://{host.host}{port}")


_DEFAULT_CONFIG_FILES = [str(pathlib.Path("classiq", "config.ini"))]
if os.name == "posix":
    # Unix convensions:
    #   System-wide configuration rests in "/etc"
    #       either as "/etc/program_name.conf" or as "/etc/program_name/some_name"
    #   User-wide configuration rests in "~/.config"
    # Order matters - System-wide is most general, than user-wide,
    #   and than folder-specific configration
    _DEFAULT_CONFIG_FILES = [
        "/etc/classiq/config.ini",
        "~/.config/classiq/config.ini",
        "/etc/classiq.conf",
        "~/.config/classiq.conf",
    ] + _DEFAULT_CONFIG_FILES


def init(args: Optional[Union[str, List[str]]] = None) -> Configuration:
    """Initialize the configuration object.

    Args:
        args (): Non-default arguments.

    Returns:
        Initialized configuration object.
    """
    arg_parser = configargparse.ArgParser(default_config_files=_DEFAULT_CONFIG_FILES)

    arg_parser.add_argument(
        "--classiq-config-file",
        is_config_file=True,
        help="Configuration file path",
        env_var="CLASSIQ_CONFIG_FILE",
    )
    arg_parser.add_argument(
        "--classiq-host",
        help="The URL of Classiq's backend host",
        env_var="CLASSIQ_HOST",
        default="https://classiquantum.com",
    )

    parsed_args, _ = arg_parser.parse_known_args(args=args)
    return Configuration(host=parsed_args.classiq_host)
