import argparse
import multiprocessing
from plugin_loader import PluginLoader
from calculator.logger import logger  

def run_plugin(plugin_name, args):
    """Run a plugin and log the results."""
    plugin_loader = PluginLoader()
    plugin = plugin_loader.get_plugin(plugin_name)
    
    if not plugin:
        logger.error(f"Plugin '{plugin_name}' not found.")
        return f"Plugin '{plugin_name}' not found."

    try:
        result = plugin.execute(*args)
        logger.info(f"Executed plugin: {plugin_name}({', '.join(map(str, args))}) = {result}")
        return f"Result of {plugin_name}({', '.join(map(str, args))}): {result}"
    except Exception as e:
        logger.error(f"Error executing plugin '{plugin_name}': {e}")
        return f"Error executing plugin '{plugin_name}': {e}"

def main():
    parser = argparse.ArgumentParser(description="Run plugins from the plugins folder.")
    parser.add_argument(
        "--plugin",
        type=str,
        required=True,
        help="Name of the plugin to execute (e.g., addition_plugin)"
    )
    parser.add_argument(
        "--args",
        nargs="+",
        type=float,
        required=True,
        help="Arguments for the plugin (e.g., 2 3)"
    )
    args = parser.parse_args()

    process = multiprocessing.Process(
        target=run_plugin,
        args=(args.plugin, args.args)
    )

    process.start()
    process.join()

    if process.exitcode == 0:
        logger.info("Plugin execution completed successfully.")
        print("Plugin execution completed.")
    else:
        logger.error("Plugin execution failed.")
        print("Plugin execution failed.")

if __name__ == "__main__":
    main()