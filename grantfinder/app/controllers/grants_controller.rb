class GrantsController < ApplicationController
    def index
	@start = params['start'].to_i
        @grant = Grant.all[@start, 15]
    end
    def show
        @grant = Grant.find(params[:id])
    end
end
