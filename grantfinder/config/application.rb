require_relative 'boot'

searchEngineJob = fork do
  exec "python3 #{Kernel.__dir__}/../data_mining/searchLSA.py"
end
Process.detach(searchEngineJob)
puts "------------------------"
puts "SEARCH PROCESS STARTED"
puts "------------------------"

require 'rails/all'

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

module Grantfinder
  class Application < Rails::Application
    # Initialize configuration defaults for originally generated Rails version.
    config.load_defaults 5.2
    # Settings in config/environments/* take precedence over those specified here.
    # Application configuration can go into files in config/initializers
    # -- all .rb files in that directory are automatically loaded after loading
    # the framework and any gems in your application.
  end
end
