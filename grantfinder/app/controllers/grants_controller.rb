class GrantsController < ApplicationController
    skip_before_action :authenticate_user!, only: [:index]
    def index
	@start = params['start'].to_i
        @grant = Grant.all[@start, 15]
    end
    def show
        @grant = Grant.find(params[:id])

    end
end
