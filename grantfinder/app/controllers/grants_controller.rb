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
						scores = Array.new
            search_results.each do |result|
                grants.push(Grant.find(result[0])) # Retrieve the grant from the database 
								scores.push(((result[1]*10000).round)/100)
            end
            # puts grants
        end

				@page = params['page'].to_i
				@query = params['query']
				@total = grants.length
				@score = scores[ @page * 15, 15 ]

				@grant = grants[ @page * 15, 15 ]
        #@grant = grants # These are the grant results from the search
    end

    def show
        @grant = Grant.find(params[:id])
    end
    # def search
    #     @start = params['page'].to_i
    #     @grant = Grant.all[@start, 15]
    #     puts(params[:query])
    # end
end
