Rails.application.routes.draw do
  
  root to: 'pages#home'
  
  devise_for :users
  
  get 'home', to: 'pages#home', as: 'home'
  get 'results', to: 'grants#index', as:'results'
  get 'results/:id', to: 'grants#show', as: 'result'
  get 'results', to: 'grants#index', as: 'back'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
