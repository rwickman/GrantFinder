Rails.application.routes.draw do
  root to: 'pages#home'
  get 'home', to: 'pages#home', as: 'home'
  get 'results', to: 'grants#index', as:'results'
  # get 'results/:search', to: 'grants#search', as: 'results_search'
  get 'results/:id', to: 'grants#show', as: 'result'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
