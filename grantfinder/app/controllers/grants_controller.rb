class GrantsController < ApplicationController
    def index
        @grant = Grant.all
    end
    def show
        @grant = Grant.find(params[:id])
    end
end
