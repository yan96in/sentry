import React from 'react';
import {shallow} from 'enzyme';
import ProjectPlugins from 'app/views/projectPlugins/projectPlugins';

describe('ProjectPlugins', function() {
  let wrapper;
  let plugins = TestStubs.Plugins();
  let org = TestStubs.Organization();
  let project = TestStubs.Project();
  let params = {
    orgId: org.slug,
    projectId: project.slug,
  };

  it('renders', function() {
    wrapper = shallow(
      <ProjectPlugins
        params={params}
        plugins={plugins}
        organization={{features: ['integrations-v3']}}
      />
    );

    expect(wrapper).toMatchSnapshot();
  });

  it('has loading state', function() {
    wrapper = shallow(
      <ProjectPlugins
        params={params}
        loading
        plugins={[]}
        organization={{features: ['integrations-v3']}}
      />
    );

    expect(wrapper.find('LoadingIndicator')).toHaveLength(1);
  });

  it('has error state when plugins=null and loading is true', function() {
    wrapper = shallow(
      <ProjectPlugins
        params={params}
        plugins={null}
        loading
        organization={{features: ['integrations-v3']}}
        error={new Error('An error')}
      />
    );

    expect(wrapper.find('RouteError')).toHaveLength(1);
  });

  it('has error state when plugins=[]', function() {
    wrapper = shallow(
      <ProjectPlugins
        params={params}
        plugins={[]}
        loading
        organization={{features: ['integrations-v3']}}
        error={new Error('An error')}
      />
    );

    expect(wrapper.find('RouteError')).toHaveLength(1);
  });
});
