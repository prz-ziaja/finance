from SPFinance.scraper.common import get_parser
import importlib

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    plugin_name = args.pop("plugin_name")
    plugin_module = importlib.import_module(f"SPFinance.scraper.plugins.{plugin_name}")
    plugin = getattr(plugin_module, plugin_name.split('.')[-1])
    plugin(**args).run()

if __name__ == "__main__":
    main()