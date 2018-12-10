require 'socket'
require 'json'

class GrantsController < ApplicationController
    def index
	    @start = params['start'].to_i
        #@grant = Grant.all[@start, 15]

        # Create a TCP Socket to communicate with search engine (searchLSA.py)
        host = Socket.gethostname
        port = 50001
        s = TCPSocket.new host, 50001
        s.puts(params[:query])
        json_results = ''
        begin
            while line = s.gets
                json_results += line
            end
        rescue
        end
        s.close()
        if !json_results.nil?
            search_results = JSON.parse(json_results)
            grants = Array.new
            search_results.each do |result|
                grants.push(Grant.find(result[0])) # Retrieve the grant from the database 
            end
            # puts grants
        end

        @grant = grants # These are the grant results from the search
    end

    def show
        @grant = Grant.find(params[:id])
    end
    # def search
    #     @start = params['start'].to_i
    #     @grant = Grant.all[@start, 15]
    #     puts(params[:query])
    # end
end
