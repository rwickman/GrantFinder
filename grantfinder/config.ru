# This file is used by Rack-based servers to start the application.

require_relative 'config/environment'


searchEngineJob = fork do
    exec "pwd;python3 #{Kernel.__dir__}/data_mining/searchLSA.py"
end
Process.detach(searchEngineJob)
puts "------------------------"
puts "SEARCH PROCESS STARTED"
puts "------------------------"

run Rails.application
