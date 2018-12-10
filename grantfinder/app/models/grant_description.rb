# == Schema Information
#
# Table name: grant_descriptions
#
#  id          :integer          not null, primary key
#  description :text
#  term_vector :text
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#  grant_id    :integer
#
# Indexes
#
#  index_grant_descriptions_on_grant_id  (grant_id)
#

class GrantDescription < ApplicationRecord
    belongs_to :grant,
        class_name: "Grant",
        foreign_key: "grant_id",
        inverse_of: :description

end
