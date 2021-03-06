# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

# grant_1= Grant.new(title:"NIH Small Research Grant Program (Parent R03 Clinical Trial Not Allowed)", release_date:"11/5/2018", expired_date:"1/8/2020", document_number: "PA-19-052", document_type:"PA", activity_code:"RO3", clinical_trails:"Not_Allowed", url: "https://grants.nih.gov/grants/guide/pa-files/PA-19-052.html")
# grant_1.description = GrantDescription.new(description: "National Institutes of Health (NIH)The NIH Small Research Grant Program supports small research projects that can be carried out in a short period of time with limited resources. This program supports different types of projects including pilot and feasibility studies; secondary analysis of existing data; small, self-contained research projects; development of research methodology; and development of new research technology. This Funding Opportunity Announcement does not accept applications proposing clinical trial(s).", term_vector: '["nih", "small", "research", "grant", "program", "parent", "r03", "clinical", "trial", "not", "allowed", "national", "institutes", "of", "health", "nih", "small", "research", "grant", "program", "supports", "research", "projects", "that", "can", "be", "carried", "out", "in", "short", "period", "of", "time", "limited", "this", "program", "supports", "different", "types", "of", "including", "pilot", "and", "feasibility", "secondary", "analysis", "of", "existing", "research", "development", "of", "research", "and", "development", "of", "new", "research", "funding", "opportunity", "announcement", "does", "not", "applications", "proposing", "clinical"]')
# grant_1.save!

# grant_2= Grant.new(title:"Research Project Grant (Parent R01 Clinical Trial Required)", release_date:"11/5/2018", expired_date:"1/8/2020", document_number: "PA-19-055", document_type:"PA", activity_code:"R01", clinical_trails:"Required", url: "https://grants.nih.gov/grants/guide/pa-files/PA-19-055.html")
# grant_2.description = GrantDescription.new(description:"The NIH Research Project Grant supports a discrete, specified, circumscribed project in areas representing the specific interests and competencies of the investigator(s). This Parent Funding Opportunity Announcement requires that at least 1 clinical trial be proposed. The proposed project must be related to the programmatic interests of one or more of the participating NIH Institutes and Centers (ICs) based on their scientific missions. Applicants should note that some ICs (see Related Notices) only accept applications proposing mechanistic studies that meet NIH's definition of a clinical trial through this funding opportunity announcement.", term_vector: '["research", "project", "grant", "parent", "r01", "clinical", "trial", "required", "the", "nih", "research", "project", "grant", "supports", "circumscribed", "project", "in", "areas", "representing", "the", "specific", "and", "competencies", "of", "the", "this", "parent", "funding", "announcement", "requires", "that", "at", "least", "clinical", "trial", "be", "proposed", "project", "must", "be", "related", "to", "the", "programmatic", "interests", "of", "one", "or", "of", "the", "participating", "nih", "institutes", "and", "centers", "ics", "based", "on", "scientific", "should", "note", "that", "some", "ics", "see", "related", "notices", "only", "accept", "proposing", "mechanistic", "studies", "that", "meet", "definition", "of", "clinical", "through", "this", "funding", "opportunity"]')
# grant_2.save!

require 'csv'
require 'json'

csv_text = File.read(Rails.root.join('lib', 'seeds', '11_5_2018-AllGuideResultsReport.csv'))
json_text = File.read(Rails.root.join('lib', 'seeds', 'grant_descriptions.json'))

csv = CSV.parse(csv_text, :headers => true)
grant_descriptions = JSON.parse(json_text)

empty = Array.new
descriptions_arr = Array.new

grant_descriptions.each do |row|
    if row[1]["description"] == "" or row[1]["term_vector"] == ""
         empty.push(row[0].to_i) #Stores all the empty items' id
    else
        desc = GrantDescription.new
        desc.description = row[1]["description"]
        desc.term_vector = row[1]["term_vector"]
        descriptions_arr.push(desc)
    end
end

j = 0
csv.each do |row|
    if !empty.include? j
        grant = Grant.new
        grant.title =  row['﻿Title']
        grant.release_date = row['Release_Date']
        grant.expired_date = row['Expired_Date']
        grant.document_number = row["Document_Number"]
        grant.document_type = row["Document_Type"]
        grant.activity_code = row["Activity_Code"]
        grant.clinical_trails = row["Clinical_Trials"]
        grant.url = row["URL"]
        grant.description = descriptions_arr.shift
        grant.save!
    end
    j += 1
end

user_1 = User.new(email: 'user1@email.com', password: 'dddddd')
user_1.save!

user_2 = User.new(email: 'user2@email.com', password: 'dddddd')
user_2.save!